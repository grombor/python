import socket
import threading
from server_files.server_config import get_config

class Server:
    """ Main server API class """

    # Get data from config file
    HOST, PORT, HEADER_SIZE, CODING = get_config()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    # Initialize lists
    clients = []
    nicknames = []


    def broadcast(self, message):
        """ Send message to all clients """

        print(f'message to all >> {message}')
        for client in self.clients:
            client.send(message.encode(self.CODING))


    def handle_client(self, client, nickname):
        """ Handle client connection """

        while True:
            try:
                message = client.recv(self.HEADER_SIZE)
                self.broadcast(f"{nickname}: {message.decode(self.CODING)}")
            except:
                client_index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                self.broadcast(f"{client} left.")
                nickname = self.nicknames.index(client_index)
                print(f"{nickname} left")
                break


    def receive(self) -> None:
        print(f'Server is running.')
        while True:
            client, address = self.server.accept()
            print(f'connected {str(address)}')
            client.send('--NICK'.encode(self.CODING))
            nickname = client.recv(self.HEADER_SIZE).decode(self.CODING)
            self.nicknames.append(nickname)
            self.clients.append(client)
            message = f'<< {nickname} joined >>'
            self.broadcast(message)
            thread = threading.Thread(target=Server().handle_client, args=(client, nickname))
            thread.start()

# Run server
start_server = Server().receive()
start_server()
