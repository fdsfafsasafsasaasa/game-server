from client.net import send
from client import player

import pickle

import time

import pygame

pygame.init()

while True:
    print(pickle.loads(send(player.encode())))
    time.sleep(1)