from client.net import send
from client import player
import pickle
import pygame

pygame.init()

display_width = 800
display_height = 800

window = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        tick = player.tick(event)
    
    window.fill((255,250,250))

    response = pickle.loads(send(player.encode()))

    data = response[1]

    pygame.draw.circle(window, data['color'], (data['x'], data['y']), 5)

    player.draw(window)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()