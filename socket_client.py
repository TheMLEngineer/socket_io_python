import socket

client_socket = socket.socket()
# IP address and port needed as args as a tuple
client_socket.connect(('localhost' , 9999))