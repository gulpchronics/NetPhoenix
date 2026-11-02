
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

routers = [
    {
        "name": "R1",
        "device": {
            "device_type": "vyos",
            "host": "192.168.135.200",
            "username": "vyos",
            "port": 22
        }
    },
    {
        "name": "R2",
        "device": {
            "device_type": "vyos",
            "host": "192.168.135.201",
            "username": "vyos",
            "port": 22
        }
    }
]

password = getpass("Enter VyOS password: ")

print("\n========== NETPHOENIX NETWORK MONITOR ==========")
print("Time:", datetime.now())
print("Checking router connectivity...\n")

for router in routers:
    name = router["name"]
    device = router["device"].copy()
    device["password"] = password

    print(f"\nConnecting to {name} ({device['host']})")

    try:
        connection = ConnectHandler(**device)

        print(f"[SUCCESS] SSH connected to {name}")

        output = connection.send_command("show ip ospf neighbor")

        print(f"\nOSPF Neighbor Status - {name}:")
        print(output)

        connection.disconnect()

    except Exception as error:
        print(f"[ERROR] {name}: {error}")

print("\n========== MONITORING COMPLETED ==========")
