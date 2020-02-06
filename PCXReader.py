import pygame
import math
import random
import os

WIDTH = 750
HEIGHT = 600

RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,200)
YELLOW = (255,255,0)
ORANGE = ()
BLACK = (0,0,0)
GRAY = (125,119,119)
LIGHTGRAY = (150,150,150)
DARKGRAY = (60,60,60)
WHITE = (255,255,255)

size = (WIDTH, HEIGHT)
pygame.init()
running = True
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.Font(None, 28)
  


files = []
for(dirpath, dirnames, filenames) in os.walk('data'):
    files.extend(filenames)
    break
print(files)

for file in files:
    data = file.split(".")
    fname = data[0]
    ext = data[1]
    if ext == "PCX":
        pcx = pygame.image.load(os.path.join('data', file))  
        pygame.image.save(pcx, os.path.join('output', fname + '.png'))

"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         
    screen.fill(DARKGRAY)
    screen.blit(pcx, (0,0))
    clock.tick(FPS)    
    pygame.display.flip() 
"""
pygame.quit()