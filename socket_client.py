import socket

client_socket = socket.socket()
# IP address and port needed as args as a tuple
client_socket.connect(('localhost' , 9999))

# Sending A name to server
name = input('Enter Your Name :')
client_socket.send(bytes(name , 'utf-8'))

# Printing what client received from server
# 1024 is buffer size here
print(client_socket.recv(1024))