"""
-> Sockets 
Are endpoints of the communication channels or basically,
the endpoints that talk to each other.
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
? AF_INET : states we want internet socket rather than UNIX socket
? SOCK_STREAM : TCP
? SOCK_DGRAM  : UDP
"""

"""
~ Server Socket Methods :
>>  bind() : Binds the address that consists of hostname and port to the socket
>> listen(): Waits for a message or a signal
>> accept(): Accepts the connection with a client

~ Client Socket Method : 
>> connect(): Client attempts to connect to a server which then has to accept this with the respective method.

~ Other Methods :
>> recv() : receive a TCP message
>> send() : send a TCP message
>> recvfrom() : receive a UDP message
>> sendto() : senf a UDP message
>> close() : close a socket
>> gethostname() : returns hostname of a socket
"""


