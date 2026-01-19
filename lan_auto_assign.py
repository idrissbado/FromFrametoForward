"""
LAN Auto Assignment Script
Author: idrissbado
Generates MAC/IP assignments and subnetting for a small LAN.
"""
import random

def random_mac(prefix):
    return prefix + ":" + ":".join(f"{random.randint(0,255):02X}" for _ in range(4))

def assign_lan():
    mac_prefix = "00:AA:BB:CC"
    devices = [
        ("Router", 1),
        ("Switch 1", 2),
        ("Switch 2", 3),
        ("PC 1", 11),
        ("PC 2", 12),
        ("PC 3", 13),
        ("PC 4", 14),
        ("Printer", 21),
        ("Wi-Fi AP", 129),
        ("Wireless Dev 1", 130),
        ("Wireless Dev 2", 131),
    ]
    print("\nDevice Assignments:")
    print(f"{'Device':<16} {'MAC Address':<20} {'IP Address':<16}")
    for name, host in devices:
        mac = random_mac(mac_prefix)
        ip = f"192.168.10.{host}"
        print(f"{name:<16} {mac:<20} {ip:<16}")
    print("\nWired subnet: 192.168.10.0/25 (1-126)")
    print("Wireless subnet: 192.168.10.128/27 (129-158)")
    print("Default gateway: 192.168.10.1 (Router)")
    print("DHCP can be enabled on router or AP for dynamic assignment.")

if __name__ == "__main__":
    assign_lan()
