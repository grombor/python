import json
from server_files.server_config import *
from server_files.commands_list import get_commands_list


def show_help():
    msg = json.dumps(get_commands_list()).encode(CODING)
    return msg


def show_info():
    msg = json.dumps({"version": VERSION}).encode(CODING)
    return msg


def show_uptime():

    def calculate_uptime(time):
        return int((datetime.now() - time).total_seconds())

    uptime = {"uptime": str(calculate_uptime(UPTIME))+' seconds'}
    msg = json.dumps(uptime).encode(CODING)
    return msg


def show_unknown_command():
    msg = json.dumps("Unknown command. Try type 'help' for more info.").encode(CODING)
    return msg


def stop_server(client_socket):
    msg = "Server was stopped by client."
    print(msg)
    client_socket.send(msg.encode(CODING))
    client_socket.close()
    

def handle_command(command, client_socket):
    if command in ("quit", "stop"):
        stop_server(client_socket)
        quit()
    if command == "help":
        command = show_help()
        client_socket.send(command)
    if command == "info":
        command = show_info()
        client_socket.send(command)
    if command == "uptime":
        command = show_uptime()
        client_socket.send(command)
    pass


def handle_message(msg, client_socket):
    msg = msg.encode(CODING)
    client_socket.send(msg)

