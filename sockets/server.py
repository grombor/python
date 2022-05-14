# Usefull links:
# https://realpython.com/python-sockets/#background
# https://www.programiz.com/python-programming/online-compiler/
# https://jsonformatter.curiousconcept.com/#
# https://www.geeksforgeeks.org/tcp-3-way-handshake-process/


# Simple echo server

import socket
from server_files.commands_list import get_commands_list
from server_files.server_functions import show_help, show_info, show_uptime, show_unknown_command, stop_server, handle_command
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
    msg = client_socket.recv(HEADER_SIZE).decode(CODING).lower()
    if msg in get_commands_list().keys():
        if msg in ("quit", "stop"):
            handle_command(msg, client_socket)
            break
        elif msg in ("help", "info", "uptime"):
            handle_command(msg, client_socket)
    else:
        msg = show_unknown_command()
        client_socket.send(msg)


