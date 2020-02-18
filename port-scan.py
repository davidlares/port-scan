#!/usr/bin/python

import socket
# defining socket object (AF_INET - Ipv4 addresses, SOCK_STREAM - TCP packets)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# perform the connection within 2 secs
socket.setdefaulttimeout(2)

# asking for the value
host = raw_input("[*] Enter host to scan: ")
port = int(raw_input("[*] Enter port to scan: "))

# performing the connection
def connection(port):
    # connection evaluation
    if sock.connect_ex((host, port)):
        print("Port %d - Closed" % port)
    else:
        print("Port %d - Open" % port)

# calling the function
connection(port)
