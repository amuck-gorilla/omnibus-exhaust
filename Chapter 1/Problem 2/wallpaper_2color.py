import pygame, math, sys
from pygame.locals import *
corna = int(sys.argv[1])
cornb = int(sys.argv[2])
side = int(sys.argv[3]) % 100

pygame.init()

windowSurface = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption('WALLPAPER')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

for i in range(1, 101):
    for j in range(1, 101):
        x = corna + i * side/100
        y = cornb + j * side/100
        c = math.floor(x*x + y*y)
        if c % 3 == 0:
            pygame.draw.rect(windowSurface, RED, ((i-1)*10, (j-1)*10, 10, 10))
        elif c % 3 == 1:
            pygame.draw.rect(windowSurface, GREEN, ((i-1)*10, (j-1)*10, 10, 10))
        else:
            pygame.draw.rect(windowSurface, BLUE, ((i-1)*10, (j-1)*10, 10, 10))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
