import socket
import getpass
from content import admin_password


class Group:
    def __init__(self , group_name) -> None:
        self.group_name = group_name
        self.group_messages = []
        print(f'{group_name} Initialized ... ')
    def create(self , ip_address = 'localhost' , port = 9999):
        client_socket = socket.socket()
        # IP address and port needed as args as a tuple
        client_socket.connect((ip_address , port))
        print(f'{self.group_name} Created ... ')
        return client_socket
    def send_messages(self , message = bytes('Test Message' , 'utf-8')):
        socket_to_send = Group.create(self)
        # Formatting Message
        message = bytes(f'{message}' , 'utf-8')
        socket_to_send.send(message)
        self.group_messages.append('Sent Message : ' + str(message))
    def receive_messages(self , message = bytes('Test Message' , 'utf-8')):
        print(f'Group Name : {self.group_name}')
        rc_msg = Group.create(self).recv(1024)
        print('Received Message : ' , Group.create(self).recv(1024))
        self.group_messages.append('Received Message : ' + str(rc_msg))
    def print_messages(self):
        for msg in self.group_messages:
            print(msg)




def create_user(user_dictionary , user_name , password):
    user_dictionary[user_name] = password
def modify_user_name(user_dictionary , new_user_name , old_user_name):
    user_dictionary[new_user_name] = user_dictionary.pop(old_user_name)
def modify_password(user_dictionary , user_name , new_password):
    user_dictionary[user_name] = password
def delete_user(user_dictionary , user_name):
    del user_dictionary[user_name]

# Checking If the person logging in is ADMIN
user_name = input('Kindly Enter Your Username : ')
password = getpass.getpass('Kindly Enter Your Password : ')

user_dictionary = {'Karthik' : '1234'}

if user_name == 'admin' and password == admin_password :
    user = '<ADMIN>'
    ack = input('You have logged in as admin , Want to Manage App [Y/N] : ')

    while input('Want To Manage [Y/N] :').upper() == 'Y':
        if ack.upper() == 'Y':
            print('1. Create User')
            print('2. Modify User Name')
            print('3. Modify Password')
            print('4. Delete User')
            option = int(input('Kindly Select Your option : '))

            if option == 1:
                create_user_name = input('Kindly Enter Username You want to create : ')
                create_password = getpass.getpass(f'Kindly Enter Password of {create_user_name}: ')
                create_user(user_dictionary , create_user_name , create_password)
            elif option == 2:
                old_user_name = input('Kindly Enter Old Username  : ')
                new_user_name = input('Kindly Enter New Username  : ')
                modify_user_name(user_dictionary , new_user_name , old_user_name)      
            elif option == 3:
                old_user_name = input('Kindly Enter Username You : ')
                new_password = getpass.getpass('Kindly Enter New Password : ')
            elif option == 4:
                delete_user_name = input('Kindly Enter Username You Want to delete : ')
                delete_user(user_dictionary , delete_user_name)


# Normal User Login
elif user_dictionary[user_name] == password:
    print(f'Logged In As {user_name} ...')
    # Creating local group object
    group_obj = Group('Avengers')
    print('Sending 3 random messages ... ')
    group_obj.send_messages('First Message')
    group_obj.send_messages('Second Message')
    group_obj.send_messages('Third Message')
    print('Message sent. Check the other endpoint if it has been received.')

else:
    print('Kindly check auth credentials')

#client_socket = socket.socket()
# IP address and port needed as args as a tuple
#client_socket.connect(('localhost' , 9999))

# Sending A name to server
#name = input('Enter Your Name :')
#client_socket.send(bytes(name , 'utf-8'))

# Printing what client received from server
# 1024 is buffer size here
#print(client_socket.recv(1024))