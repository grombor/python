# Usefull links:
# https://realpython.com/python-sockets/#background
# https://www.programiz.com/python-programming/online-compiler/
# https://jsonformatter.curiousconcept.com/#
# https://www.geeksforgeeks.org/tcp-3-way-handshake-process/


# Simple echo server
import json
import socket
from server_files.commands_list import get_commands_list
from server_files.server_functions import handle_command, handle_message
from server_files.server_config import *

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(5)

msg = f"Server {HOST} is starting on port {PORT}."
print(msg)
print("-"*25)
msg = f"Welcome to the {HOST} server!"
print("-"*25)
print(msg)
msg = msg.encode(CODING)


client_socket, client_address = socket.accept()
print(f"Connection from {client_address[0]}:{client_address[1]} has been established.")
client_socket.send(msg)
while True:
    received_msg = json.loads(client_socket.recv(HEADER_SIZE))
    nickname = received_msg["nickname"]
    message = received_msg["message"]

    if message in get_commands_list().keys():
        if message in ("quit", "stop"):
            handle_command(message, client_socket)
            break
        elif message in ("help", "info", "uptime"):
            handle_command(message, client_socket)
    else:
        print(f"{nickname}: {message}")
        handle_message("ok", client_socket)



