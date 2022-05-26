import json
from server_files.server_config import *
from server_files.commands_list import get_commands_list, show_commands


class Server:

    def get_help(self):
        """ Show all available commands. """

        return get_commands_list()


    def get_info(self):
        """ Show server version. """

        return f"version: {VERSION}"


    def get_uptime(self) -> str:
        """ Show how much time server is online. """

        def calculate_uptime(time):
            return int((datetime.now() - time).total_seconds())

        return f"uptime: {str(calculate_uptime(UPTIME))} seconds"


    def show_unknown_command(self):
        """ Print help for invalid command. """

        return "Unknown command. Try type '--help' for more info."


    def stop_server(self, client_socket):
        """ Stop server function. """

        msg = dict()
        msg["message"] = "Server was stopped by client."
        client_socket.send(json.dumps(msg).encode(CODING))
        client_socket.close()


    def handle_command(self, command, client_socket):
        """ Handling commands logic. """

        if command in ("--quit", "--stop"):
            self.stop_server(client_socket)
        if command == "--help":
            msg = {
                "id": "server",
                "message": show_commands()
            }
            client_socket.send(json.dumps(msg).encode(CODING))
        if command == "--info":
            msg = {
                "id": "server",
                "message": self.get_info()
            }
            client_socket.send(json.dumps(msg).encode(CODING))
        if command == "--uptime":
            msg = {
                "id": "server",
                "message": self.get_uptime()
            }
            client_socket.send(json.dumps(msg).encode(CODING))

        pass


    def greetings(self):
        """ Show greetings. """

        return f"Welcome to the {HOST} server! :: Type '--help' for info.\n"


    def handle_message(self, client_socket, msg=""):
        """ Send message to client. """

        msg = {
            "id": "server",
            "message": msg
        }
        msg = json.dumps(msg).encode(CODING)
        print(f"server: {msg}")
        client_socket.send(msg)
