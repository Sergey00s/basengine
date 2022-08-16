from asyncio import events
from curses.textpad import rectangle
from unittest import runner
import pygame

pygame.init()

window = pygame.display.set_mode((1000, 400))

running = True
posx = 0
posy = 1

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
       
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        posx -= 1 
    if keys[pygame.K_RIGHT]:
        posx += 1
    if keys[pygame.K_UP]:
        posy -= 1
    if keys[pygame.K_DOWN]:
        posy += 1

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), (posx, posy, 50, 50))
    pygame.display.update()
