#!/usr/bin/python3

import socket
from termcolor import colored

# defining socket object (AF_INET - Ipv4 addresses, SOCK_STREAM - TCP packets)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# perform the connection within 2 secs
socket.setdefaulttimeout(2)

# asking for the value
host = input("[*] Enter host to scan: ")
# port = int(input("[*] Enter port to scan: "))

# performing the connection
def connection(port):
    # connection evaluation
    if sock.connect_ex((host, port)):
        print(colored("[!] Port %d - Closed" % port, 'red'))
    else:
        print(colored("[!] Port %d - Open" % port, 'green'))

# port range (known ports)
for port in range(1,1024):
    # port evaluation
    connection(port)
