import math
import pygame
import sys
from pygame.locals import *

pygame.init()
WINDOWWIDTH = 500
WINDOWHEIGHT = 300
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Graphs')

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
SOMETHING = (235, 123, 56)
windowSurface.fill(BLACK)

# y = x
startpoint = (0, WINDOWHEIGHT)
endpoint = (WINDOWWIDTH, 0)
pygame.draw.line(windowSurface, BLUE, startpoint, endpoint)

# y = x**2
points_exp = []
for x in range(WINDOWWIDTH):
  y = x**2
  points_exp.append((x, WINDOWHEIGHT - y))
pygame.draw.lines(windowSurface, YELLOW, False, points_exp)

# y = 2**x
points_pwr = []
for x in range(WINDOWWIDTH):
  y = 2**x
  points_pwr.append((x, WINDOWHEIGHT - y))
pygame.draw.aalines(windowSurface, GREEN, False, points_pwr)

# y = log x
points_log = []
for x in range(1, WINDOWWIDTH):
  y = math.log(x, 2)
  points_log.append((x, WINDOWHEIGHT - y))
pygame.draw.lines(windowSurface, WHITE, False, points_log)

# y = x * log x
points_lg = []
for x in range(1, WINDOWWIDTH):
  y = x * math.log(x, 2)
  points_lg.append((x, WINDOWHEIGHT - y))
pygame.draw.lines(windowSurface, RED, False, points_lg)

# y = x!
points_f = []
for x in range(1, WINDOWWIDTH):
  y = math.factorial(x)
  points_f.append((x, WINDOWHEIGHT - y))
pygame.draw.lines(windowSurface, SOMETHING, False, points_f)

pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)