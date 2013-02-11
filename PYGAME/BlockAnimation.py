import pygame, sys, time
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# Set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
RIGHT = 6
LEFT = 4

MOVESPEED = 4

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the block data structure
b1 = {'rect' : pygame.Rect(300, 80, 55, 60), 'color' : RED, 'dir' : UPRIGHT}
b2 = {'rect' : pygame.Rect(200, 250, 45, 30), 'color' : GREEN, 'dir' : UPLEFT}
b3 = {'rect' : pygame.Rect(100, 150, 67, 60), 'color' : BLUE, 'dir' : DOWNLEFT}
b4 = {'rect' : pygame.Rect(10, 300, 24, 45), 'color' : YELLOW, 'dir' : DOWNRIGHT}
b5 = {'rect' : pygame.Rect(250, 340, 200, 10), 'color' : WHITE, 'dir' : RIGHT}
blocks = [b1, b2, b3, b4]

# Run the game loop
while True:
  # Check for the QUIT EVENT
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)
 
 
  # Draw the black background onto the surface
  windowSurface.fill(BLACK)
  # Draw white rectangle
  if b5['dir'] == RIGHT:
    b5['rect'].right += MOVESPEED
    if b5['rect'].right > WINDOWWIDTH:
      b5['dir'] = LEFT
  if b5['dir'] == LEFT:
    b5['rect'].left -= MOVESPEED
    if b5['rect'].left < 0:
      b['dir'] = RIGHT
  for b in blocks:
    # Move the block data structure
    if b['dir'] == DOWNLEFT:
      b['rect'].left -= MOVESPEED
      b['rect'].top += MOVESPEED
    if b['dir'] == DOWNRIGHT:
      b['rect'].left += MOVESPEED
      b['rect'].top += MOVESPEED
    if b['dir'] == UPLEFT:
      b['rect'].left -= MOVESPEED
      b['rect'].top -= MOVESPEED
    if b['dir'] == UPRIGHT:
      b['rect'].left += MOVESPEED
      b['rect'].top -= MOVESPEED
    # Check if the block has move out of the window
    if b['rect'].top < 0:
      # block has moved past the top
      if b['dir'] == UPLEFT:
        b['dir'] = DOWNLEFT
      if b['dir'] == UPRIGHT:
        b['dir'] = DOWNRIGHT
    if b['rect'].bottom > WINDOWHEIGHT:
      # block has moved past the bottom
      if b['dir'] == DOWNLEFT:
        b['dir'] = UPLEFT
      if b['dir'] == DOWNRIGHT:
        b['dir'] = UPRIGHT
    if b['rect'].left < 0:
      # block has moved passed the left side
      if b['dir'] == DOWNLEFT:
        b['dir'] = DOWNRIGHT
      if b['dir'] == UPLEFT:
        b['dir'] = UPRIGHT
    if b['rect'].right > WINDOWWIDTH:
      # block has moved passed the right side
      if b['dir'] == DOWNRIGHT:
        b['dir'] = DOWNLEFT
      if b['dir'] == UPRIGHT:
        b['dir'] = UPLEFT
    
    # Draw the blocks onto the surface
    pygame.draw.rect(windowSurface, b['color'], b['rect'])
  pygame.draw.rect(windowSurface, b5['color'], b5['rect'])

  # Draw the window onto the screen
  pygame.display.update()
  time.sleep(0.02)