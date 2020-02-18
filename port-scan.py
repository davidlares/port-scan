#!/usr/bin/python3

from termcolor import colored
from socket import *
from threading import *
import optparse

# performing the connection (refactored)
def connection(host, port):
    try:
        # defining socket object (AF_INET - Ipv4 addresses, SOCK_STREAM - TCP packets)
        sock = socket(AF_INET, SOCK_STREAM)
        # connection evaluation
        sock.connect((host, port))
        print(colored("[!] Port %d - Open" % port, 'green'))
    except Exception as e:
        print(colored("[-] %d /tcp Closed" % port, 'red'))
    finally:
        # closing socket
        sock.close()

def portScan(host, ports):
    try:
        # reaching host for getting the IP address
        ip = gethostbyname(host)
    except Exception as e:
        print("Unknown host %s" % host)

    try:
        # getting the hostname with the IP value
        name = gethostbyaddr(ip)
        print("[+] Scan results for: %s", name[0])
    except Exception as e:
        print("[+] Scan results for: %s", ip)

    # setting up the time limit
    setdefaulttimeout(1)
    for port in ports:
        # scanning with Threads
        t = Thread(target=connection, args=(host, int(port)))
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
    if(host == None) | (ports[0] == None):
        print(parser.usage)
        exit(0)
    # calling function
    portScan(host, ports)

if __name__ == "__main__":
    main()
