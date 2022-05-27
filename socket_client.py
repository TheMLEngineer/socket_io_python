import socket
import getpass
from content import admin_password

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

user_dictionary = {}

if user_name == 'admin' and password == admin_password :
    user = '<ADMIN>'
    ack = input('You have logged in as admin , Want to Manage App [Y/N] : ')

    
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


print(user_dictionary)













client_socket = socket.socket()
# IP address and port needed as args as a tuple
client_socket.connect(('localhost' , 9999))

# Sending A name to server
name = input('Enter Your Name :')
client_socket.send(bytes(name , 'utf-8'))

# Printing what client received from server
# 1024 is buffer size here
print(client_socket.recv(1024))