#!/usr/bin/python

import socket
# defining socket object (AF_INET - Ipv4 addresses, SOCK_STREAM - TCP packets)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.2.119"
port = 443

# performing the connection
def connection(port):
    # connection evaluation
    if sock.connect_ex((host, port)):
        print("Port %d - Closed" % port)
    else:
        print("Port %d - Open" % port)

# calling the function
connection(port)
