import math
import pygame
import sys
from pygame.locals import *

pygame.init()
WINDOWWIDTH = 100
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('x = y')

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

windowSurface.fill(BLACK)
points = []
for x in range(1, WINDOWWIDTH):
  y = x * math.log(x, 2)
  points.append((x, WINDOWHEIGHT - y))
pygame.draw.lines(windowSurface, BLUE, False, points)
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)