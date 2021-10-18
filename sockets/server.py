import socket

"""
https://pythonprogramming.net/sockets-tutorial-python-3/

# s variable is TCP/IP socket
# AF_INET is in reference to th family or domain, it means ipv4, as opposed to ipv6 with AF_INET6
# SOCK_STREAM means it will be a TCP socket, which is our type of socket.
# TCP means it will be connection-oriented, as opposed to connectionless.
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
