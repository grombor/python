import socket
import json
from client_files.user import User
from client_files.config import *


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))


user = User()

user.login()


while True:
    msg = socket.recv(HEADER_SIZE).decode(CODING)
    if msg == "Server was stopped by client.":
        print("Shutting down server and client connection.")
        quit()
    print(msg)
    socket.send(user.send_message())

