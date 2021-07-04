import threading

from client.net import send
from client import player

lock = threading.Lock()


# client = ClientSocketThread(SERVER, lock)

# client.start()

while True:
    input()
    send(player.encode())