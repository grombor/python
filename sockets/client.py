import socket
import json
from client_files.user import User
from client_files.config import *


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

user = User()

# Greetings and get user nickname
user.login()

# Main client loop
while True:

    # TODO: remove try/except, handle exception, test msg behavior
    try:
        msg = json.loads(socket.recv(HEADER_SIZE))
        if msg["message"] != '':
            print(msg["message"])
    except Exception:
        pass

    # Turn off client right after server.
    if msg["message"] == 'Server stopped by the user. Shutting down server and client connection.':
        quit()
    socket.send(user.send_message())

