# IaC Blueprint for Cisco Redundancy Project
devices = {
    "Router2": "192.168.10.1",
    "Switch0": "192.168.10.2"
}

# The "Intent" - Commands to ensure redundancy is active
redundancy_commands = [
    "interface GigabitEthernet0/0/1",
    "no shutdown",  # Ensures the link we turned green stays up
    "ip address 192.168.10.1 255.255.255.0",
    "exit"
]

def deploy_config(device_list, commands):
    for device, ip in device_list.items():
        print(f"Connecting to {device} at {ip}...")
        for cmd in commands:
            print(f"Applying: {cmd}")

if __name__ == "__main__":
    deploy_config(devices, redundancy_commands)
