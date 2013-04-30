import math
import pygame
import sys
from pygame.locals import *

pygame.init()
WINDOWWIDTH = 200
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('x = y')

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

windowSurface.fill(BLACK)
points = []
for x in range(1, WINDOWWIDTH):
  y = math.factorial(x)
  points.append((x, WINDOWHEIGHT - y))
pygame.draw.lines(windowSurface, BLUE, False, points)
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)