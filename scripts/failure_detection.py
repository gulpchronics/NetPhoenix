
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import re

routers = [
    {"name": "R1", "host": "192.168.135.200"},
    {"name": "R2", "host": "192.168.135.201"}
]

interfaces = ["eth0", "eth1"]
password = getpass("Enter VyOS password: ")

print("\n========== NETPHOENIX FAILURE DETECTION ==========")
print("Time:", datetime.now())

with open("failure_log.txt", "a") as log:

    for router in routers:
        device = {
            "device_type": "vyos",
            "host": router["host"],
            "username": "vyos",
            "password": password,
            "port": 22
        }

        print(f"\nConnecting to {router['name']}...")

        try:
            connection = ConnectHandler(**device)
            print(f"[CONNECTED] {router['name']}")

            for interface in interfaces:
                output = connection.send_command(
                    f"show interfaces ethernet {interface}"
                )

                if re.search(r"\bstate\s+DOWN\b", output, re.I):
                    status = "DOWN"
                elif re.search(r"\bstate\s+UP\b", output, re.I):
                    status = "UP"
                else:
                    status = "UNKNOWN"

                result = f"{router['name']} - {interface}: {status}"
                print(result)
                log.write(result + "\n")

                if status == "DOWN":
                    alert = f"[ALERT] Link failure on {router['name']} {interface}"
                    print(alert)
                    log.write(alert + "\n")

            connection.disconnect()

        except Exception as error:
            print(f"[ERROR] {router['name']}: {error}")
            log.write(f"[ERROR] {router['name']}: {error}\n")

print("\nResults saved in failure_log.txt")
print("========== MONITORING COMPLETED ==========")
