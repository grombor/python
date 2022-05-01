# Usefull links:
# https://realpython.com/python-sockets/#background
# https://www.programiz.com/python-programming/online-compiler/
# https://jsonformatter.curiousconcept.com/#
# https://www.geeksforgeeks.org/tcp-3-way-handshake-process/


# Simple echo server

import socket
from server_files.commands_list import get_commands_list
from server_files.server_functions import show_help, show_info, show_uptime, show_unknown_command, stop_server
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
            msg = stop_server()
            print(msg)
            client_socket.send(msg)
            client_socket.close()
            break
        if msg == "help":
            msg = show_help()
            client_socket.send(msg)
        if msg == "info":
            msg = show_info()
            client_socket.send(msg)
        if msg == "uptime":
            msg = show_uptime()
            client_socket.send(msg)
    else:
        msg = show_unknown_command()
        client_socket.send(msg)


