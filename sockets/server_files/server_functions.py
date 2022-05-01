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
    msg = json.dupms("Unknown command. Try type 'help' for more info.").encode(CODING)
    return msg


def stop_server():
    msg = "Server was stopped by client.".encode(CODING)
    return msg
