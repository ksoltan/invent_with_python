import pygame
import sys
from pygame.locals import *

pygame.init()
WINDOWHEIGHT = 500
WINDOWWIDTH = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('x = y')

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

windowSurface.fill(BLACK)

startpoint = (0, WINDOWHEIGHT)
endpoint = (WINDOWWIDTH, 0)
pygame.draw.line(windowSurface, BLUE, startpoint, endpoint)
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)