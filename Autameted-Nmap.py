import os

def scan_hosts():
    # Get the IP range of your LAN
    ip_range = input("Enter the IP range of your LAN (e.g., 192.168.1.0/24): ")

    # Perform a basic host discovery scan using Nmap
    print("Performing host discovery scan...")
    os.system(f"nmap -sn {ip_range}")

    # Perform a detailed scan on each discovered host
    print("Performing detailed scans on each host...")
    os.system(f"nmap -sVC -O -p- -T4 {ip_range}")

scan_hosts()
