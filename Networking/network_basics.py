"""
Networking Basics Script (Q2)
Shows IP, subnet, DNS, DHCP, and routing info using Python.
"""
import socket
import os
print("Hostname:", socket.gethostname())
print("IP Address:", socket.gethostbyname(socket.gethostname()))
print("Routing Table:")
os.system('netstat -rn')
print("DNS Servers:")
os.system('cat /etc/resolv.conf')
print("DHCP leases (if any):")
os.system('cat /var/lib/dhcp/dhclient.leases || echo "No DHCP lease file"')
