import socketserver
import pickle
import queue
import select

SERVER = ("127.0.0.1", 12001)

class GameClientServer(socketserver.ThreadingTCPServer):
    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        self.clients = set()

    def add_client(self, client):
        if client not in self.clients:
            self.clients.add(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def broadcast(self, source, data):
        for client in tuple(self.clients):
            if client is not source:
                client.schedule((source.name, data))

class GameClientHandler(socketserver.StreamRequestHandler):

    def __init__(self, request, client_address, server):
        self.buffer = queue.Queue()
        self.data = None
        super().__init__(request, client_address, server)

    def setup(self):
        super().setup()
        self.server.add_client(self)

    def handle(self):
        self.data = pickle.load(self.rfile)
    
        try:
            while True:
                self.empty_buffers()
        except (ConnectionResetError, EOFError):
            pass

    def empty_buffers(self):
        self.server.broadcast(self, self.data)
        while not self.buffer.empty():
            try:
                pickle.dump(self.buffer.get_nowait(), self.wfile)
            except BrokenPipeError:
                pass

    @property
    def name(self):
        while True: # for some reason this only works a quarter of the time
            try:
                return self.request.getpeername()
            except OSError: # why does this happen? fuck you!
                continue

    def schedule(self, data):
        self.buffer.put_nowait(data)

    def finish(self):
        self.server.remove_client(self)
        super().finish()
        
ServerInstance = GameClientServer(SERVER, GameClientHandler)

try:
    ServerInstance.serve_forever()
except KeyboardInterrupt:
    ServerInstance.server_close()