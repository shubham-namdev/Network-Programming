"""
-> Port Scanner
It tries to connect to certain ports at a host or a whole network, in order to find loopholes for future attacks.
Open ports mean a security breach.
"""

import socket

target = "127.0.0.1"

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        False

for port in range(1, 501):
    if(portscan(port)):
        print(f"Port {port} is open!")
    else:
        print(f"Port {port} is closed!")

"""
-> Threaded Port Scanner
"""
import socket
from queue import Queue
import threading

target = "127.0.0.1"

q = Queue()

for x in range(1, 5000):
    q.put(x)

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        False

def worker():
    while not q.empty():
        port = q.get()
        if(portscan(port)):
            print(f"Port {port} is open!")
       

        
for x in range(2500):
    t = threading.Thread(target=worker)
    t.start()
