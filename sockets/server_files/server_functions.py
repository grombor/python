import json
import socket
from server_files.server_config import *
from server_files.commands_list import get_commands_list, show_commands
from server_files.users import Users


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
        """ Stop server. """

        msg = {
            "id": "server",
            "message": 'Server stopped by the user. Shutting down server and client connection.',
        }
        print(msg['message'])
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

        return f".:: Welcome to the {HOST} server! :: Type '--help' for info. ::.\n"


    def handle_message(self, client_socket, msg=""):
        """ Send message to client. """

        msg = {
            "id": "server",
            "message": msg
        }
        msg = json.dumps(msg).encode(CODING)
        client_socket.send(msg)


    def is_admin(self, nickname) -> bool:
        u = Users()
        if nickname in u.get_admins():
            return True
        else:
            return False


    def listen_ (self):
        """ Main program loop """

        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind((HOST, PORT))
        socket.listen(5)

        while True:
            client_socket, client_address = socket.accept()
            print(f"Connection from {client_address[0]} has been established.")

            # Send greetings to the connected client
            self.handle_message(client_socket, self.greetings())

            received_msg = json.loads(client_socket.recv(HEADER_SIZE))
            nickname = received_msg["nickname"]
            message = received_msg["message"]

            # Check is message a command
            if message in get_commands_list().keys():
                # Kill command logic
                if message in ("--quit", "--stop"):
                    self.handle_command(message, client_socket)
                    break
                # Other command logic
                elif message in ("--help", "--info", "--uptime"):
                    self.handle_command(message, client_socket)
            else:
                # User message logic
                if self.is_admin(nickname):
                    print(print(f"(admin) {nickname}: {message}"))
                    self.handle_message(client_socket)
                else:
                    print(f"{nickname}: {message}")
                    self.handle_message(client_socket)