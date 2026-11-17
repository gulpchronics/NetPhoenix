
from netmiko import ConnectHandler
from getpass import getpass
import logging
import time

# Logging configuration
logging.basicConfig(
    filename="netphoenix.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console)

# Get router password
password = getpass("Enter VyOS password: ")

# Router details
routers = [
    {
        "name": "R1",
        "device_type": "vyos",
        "host": "192.168.135.200",
        "username": "vyos",
        "password": password,
        "recover": True,
    },
    {
        "name": "R2",
        "device_type": "vyos",
        "host": "192.168.135.201",
        "username": "vyos",
        "password": password,
        "recover": False,
    },
]

def monitor_router(router):
    connection = None

    logging.info("Checking %s (%s)", router["name"], router["host"])

    try:
        connection = ConnectHandler(
            device_type=router["device_type"],
            host=router["host"],
            username=router["username"],
            password=router["password"],
        )

        # Check interface status
        output = connection.send_command(
            "show interfaces ethernet eth0"
        )

        if "state DOWN" in output:
            logging.warning(
                "%s: eth0 is DOWN", router["name"]
            )

            # Automated recovery on R1 only
            if router["recover"]:
                logging.info(
                    "%s: Starting automated recovery",
                    router["name"]
                )

                recovery = connection.send_config_set([
                    "delete interfaces ethernet eth0 disable",
                    "commit",
                ])

                logging.info("Recovery command output:\n%s", recovery)

                # Verify recovery
                verify = connection.send_command(
                    "run show interfaces ethernet eth0"
                )

                if "state UP" in verify:
                    logging.info(
                        "%s: SUCCESS - eth0 restored",
                        router["name"]
                    )
                else:
                    logging.error(
                        "%s: Recovery attempted, but eth0 is not UP",
                        router["name"]
                    )

            else:
                logging.info(
                    "%s: Monitoring only; no recovery configured",
                    router["name"]
                )

        elif "state UP" in output:
            logging.info(
                "%s: eth0 is UP. No recovery needed",
                router["name"]
            )

        else:
            logging.warning(
                "%s: Could not determine interface status",
                router["name"]
            )

    except Exception:
        logging.exception(
            "%s: Router monitoring failed",
            router["name"]
        )

    finally:
        if connection:
            connection.disconnect()


# Main monitoring process
if __name__ == "__main__":

    logging.info("========== NetPhoenix Started ==========")

    try:
        for router in routers:
            monitor_router(router)

    except KeyboardInterrupt:
        logging.warning("Monitoring stopped by user")

    finally:
        logging.info("========== NetPhoenix Finished ==========")
