from client.player import Player

import random

player = Player(random.randint(0, 100), 30, tuple((random.randint(0, 255) for i in range(3))))

SERVER = ("127.0.0.1", 12001)