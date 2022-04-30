# Usefull links:
# https://realpython.com/python-sockets/#background
# https://www.programiz.com/python-programming/online-compiler/
# https://jsonformatter.curiousconcept.com/#
# https://www.geeksforgeeks.org/tcp-3-way-handshake-process/


# Simple echo server

import socket
from datetime import datetime
from server_files.commands_list import get_commands_list
from server_files.server_functions import show_help

HOST = socket.gethostname()
PORT = 5001
HEADER_SIZE = 1024
CODING = "utf-8"
UPTIME = datetime.now()
VERSION = "1.0.0"


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
    msg = client_socket.recv(HEADER_SIZE).decode(CODING)
    if msg in get_commands_list().keys():
        if msg in ("--quit", "--stop"):
            msg = "Server was stopped by client.".encode(CODING)
            print(msg)
            client_socket.send(msg)
            client_socket.close()
            break
        if msg == "--help":
            msg = show_help(get_commands_list()).encode(CODING)
            client_socket.send(msg)
        if msg == "--info":
            msg = f"Current server version is: {VERSION}".encode(CODING)
            client_socket.send(msg)
        if msg == "--uptime":
            msg = f"The server is online since: {UPTIME}".encode(CODING)
            client_socket.send(msg)
    else:
        msg = bytes("Unknow command. Try type --help for more info.", CODING)
        client_socket.send(msg)


