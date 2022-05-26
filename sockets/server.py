# Simple echo server
import json
import socket
from server_files.commands_list import get_commands_list
from server_files.server_functions import Server
from server_files.server_config import *

# Variables
msg = dict()
s = Server()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(5)

# Greetings
print("Server is running...")
print(s.greetings())
client_socket, client_address = socket.accept()
print(f"Connection from {client_address[0]}:{client_address[1]} has been established.")

s.handle_message(client_socket, s.greetings())


# Main server loop
while True:
    received_msg = json.loads(client_socket.recv(HEADER_SIZE))
    nickname = received_msg["nickname"]
    message = received_msg["message"]

    # Check is message a command
    if message in get_commands_list().keys():
        # Kill command logic
        if message in ("--quit", "--stop"):
            s.handle_command(message, client_socket)
            break
        # Other command logic
        elif message in ("--help", "--info", "--uptime"):
            s.handle_command(message, client_socket)
    else:
        # User message logic
        print(f"{nickname}: {message}")
        s.handle_message(client_socket)




