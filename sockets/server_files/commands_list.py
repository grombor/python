commands_list = {
    "--quit": "stop server and client",
    "--stop": "stop server and client",
    "--help": "show this help",
    "--info": "show server version and creation date",
    "--uptime": "show server lifetime",
}


def get_commands_list():
    return commands_list


def show_commands():
    text = "\n"
    for key, value in commands_list.items():
        text += f"{key}: {value} \n"
    return text


