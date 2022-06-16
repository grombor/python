import socket
import threading
import json
from client_files.user import User
from client_files.config import *




# user = User()
#
# # Greetings and get user nickname
# user.login()
#
# # Main client loop
# while True:
#
#     # TODO: remove try/except, handle exception, test msg behavior
#     try:
#         msg = json.loads(socket.recv(HEADER_SIZE))
#         if msg["message"] != '':
#             print(msg["message"])
#     except Exception as e:
#         print(e)
#
#     # Turn off client right after server.
#     if msg["message"] == 'Server stopped by the user. Shutting down server and client connection.':
#         quit()
#     socket.send(user.send_message())

class Client:
    """ Main client class """

    nickname = ''

    def connect_to_server(self):
        """ Connect to the server """

        # Main client loop
        while True:
            try:
                message = client.recv(1024).decode('utf8')
                if message == '--NICK':
                    print("Enter your nickname:")
                    self.nickname = input()
                    client.send(self.nickname.encode('utf8'))
                else:
                    print(message)
            except:
                print(f'Error!')
                client.close()
                break


    def send_message(self, client_id):
        message = f'{input("")}'
        client_id.send(message.encode('utf8'))


# Prepare protocols to connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

# Create thread for client_connect
client_connect_thread = threading.Thread(target=Client().connect_to_server)
client_connect_thread.start()

# Create thread for sending messages
send_message_thread = threading.Thread(target=Client().send_message, args=(client,))
send_message_thread.start()

# Run client
connect = Client().connect_to_server
connect()
