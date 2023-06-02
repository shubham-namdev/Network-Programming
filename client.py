"""
-> Creating a Client
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("127.0.0.1", 9999))
    message = s.recv(1024)
    s.close()

    print(message.decode('ascii'))

except ConnectionRefusedError: # runs if server is off
    print("Server Not Started!")
    

