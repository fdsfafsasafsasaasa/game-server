import socketserver
import pickle

SERVER = ("127.0.0.1", 12000)

class GameClientServer(socketserver.ThreadingUDPServer):
    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        self.clients = set()

    def add_client(self, client):
        if client not in self.clients:
            self.clients.add(client)

    def remove_client(self, client):
        self.clients.remove(client)

class GameClientHandler(socketserver.StreamRequestHandler):

    def handle(self):
        print(f"Got request from {self.client_address[0]}:{self.client_address[1]}.")

        data = pickle.loads(self.request[0])

        print(data)

        if self not in self.server.clients:
            self.server.add_client(self)

        print(self.server.clients)

        for client in tuple(self.server.clients):
            if client is not self:
                client.request.rfile.write(self.request[0])

    def finish(self):
        self.server.remove_client(self)
        super().finish()

ServerInstance = GameClientServer(SERVER, GameClientHandler)

try:
    ServerInstance.serve_forever()
except KeyboardInterrupt:
    ServerInstance.server_close()