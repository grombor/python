import socket
import json
from server_files.server_config import *

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

while True:
    msg = socket.recv(HEADER_SIZE).decode(CODING)
    if msg == "Server was stopped by client.":
        print("Shutting down server and client connection.")
        quit()
    print(msg)
    user_input = input("Command: ")
    msg = user_input.encode(CODING)
    socket.send(msg)

