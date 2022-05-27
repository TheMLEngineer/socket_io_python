import socket
# from wsgiref.simple_server import server_version
# 2 params , IPV4 and TCP are default params for socket()
server_socket  = socket.socket()
print('Socket Created')

# 2 Params , IP Address and port as a tuple
server_socket.bind(('localhost' , 9999))

# Listen to client
# 3 clients we listen to here
server_socket.listen(3)
print('Waiting for connections')

while True:
    client_socket , client_address = server_socket.accept()
    print('Connected with : ' , client_address)

    # Sending message to client
    client_socket.send(b'Harigato Ozaimaz')

    # Closing client socket
    client_socket.close()