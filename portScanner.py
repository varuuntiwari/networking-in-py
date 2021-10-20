import socket
import argparse
import re
import threading
from queue import Queue

def scanPort(t, n):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((t, n))
        return True
    except:
        return False

def getArgs():
    parser = argparse.ArgumentParser(usage="Example: python portScanner.py -t 127.0.0.1 -p (1-1024 or 80)")
    parser.add_argument("-t", help="Assign the target IP to scan ports on", required=True)
    parser.add_argument("-p", help="Specify a range of ports or single port to scan", required=True)
    args = parser.parse_args()
    return args

def getParams():
    args = getArgs()
    target = args.t
    if re.findall("^[0-9]{1,5}[\-][0-9]{1,5}$", args.p) != []:
        Lport, Rport = args.p.split("-", 2)
        Lport=int(Lport)
        Rport=int(Rport) + 1
    elif args.p.isnumeric():
        Lport = int(args.p)
        Rport = Lport + 1
    else:
        raise TypeError("Ports are not specified correctly, use help for more")
    
    return [target, Lport, Rport]

def runScan():
    targetIP, x, y = getParams()
    if (x < 0 or x > 65536) or (y < 0 or y > 65536) or (x > y):
        raise ValueError("Ports are not in range of a normal computer")
    
    for port in range(x, y):
        val = scanPort(targetIP, port)
        if val:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))

runScan()