import pickle
import uuid

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import pygame

class Player:
    def __init__(self, x: int, y: int, color: tuple, _uuid = uuid.uuid4()) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.uuid = str(_uuid)

    def encode(self) -> bytes:
        return pickle.dumps({"x": self.x, "y": self.y, "uuid": self.uuid, "color": self.color})

    def process_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                self.x -= 10
            elif event.key == K_RIGHT:
                self.x += 10
            elif event.key == K_DOWN:
                self.y += 10
            elif event.key == K_UP:
                self.y -= 10

    def tick(self, event):
        self.process_keys(event)

    def draw(self, screen):
        print(self.color)
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
