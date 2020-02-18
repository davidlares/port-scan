#!/usr/bin/python3

from termcolor import colored
from socket import *
from threading import *
import optparse

# defining socket object (AF_INET - Ipv4 addresses, SOCK_STREAM - TCP packets)
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# perform the connection within 2 secs
# socket.setdefaulttimeout(2)

# asking for the value
# host = input("[*] Enter host to scan: ")
# port = int(input("[*] Enter port to scan: "))

# performing the connection
def connection(port):
    # connection evaluation
    if sock.connect_ex((host, port)):
        print(colored("[!] Port %d - Closed" % port, 'red'))
    else:
        print(colored("[!] Port %d - Open" % port, 'green'))

def portScan(host, ports):
    try:
        # reaching host
        ip = gethostbyname(host)
    except Exception as e:
        print("Unknown host %s" % host)

    try:
        name = gethostbyaddr(ip)
        print("[+] Scan results for: %s", name[0])
    except Exception as e:
        print("[+] Scan results for: %s", ip)


    setdefaulttimeout(1)
    for port in ports:
        # scanning with Threads
        t = Thread(target=connScan, args=(host, int(port)))
        t.start()

def main():
    parser = optparse.OptionParser('How to use: ' + '-H <target host> -p <target port> ')
    parser.add_option('-H', dest='t_host', type='string', help='specifiy target host')
    parser.add_option('-p', dest='t_port', type='string', help='specify target ports separated by commas')
    # parsing arguments
    (options, args) = parser.parse_args()
    # specify variables
    host = options.t_host
    ports = str(options.t_port).split(',')
    # checking args
    if(t_host == None) | (t_ports[0] == None):
        print(parser.usage)
        exit(0)
    # calling function
    portScan(host, ports)

if __name__ == "__main__":
    main()

# port range (known ports)
# for port in range(1,1024):
#     # port evaluation
#     connection(port)
