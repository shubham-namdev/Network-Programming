"""
-> Creating a Server
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999)) # IP address, port number

s.listen()

print("listening...")
run = True
while run:
    client, address = s.accept()
    print(f"Connected to {address}")
    message = "Hello Client!"
    client.send(message.encode('ascii'))
    client.close()
