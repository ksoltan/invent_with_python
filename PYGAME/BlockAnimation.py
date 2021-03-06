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
blocks = [b1, b2, b3, b4]

# White wall-like block
b5 = {'rect' : pygame.Rect(200, 200, 100, 140), 'color' : WHITE, 'dir' : UPRIGHT}
b6 = {'rect' : pygame.Rect(300, 300, 140, 100), 'color' : WHITE, 'dir' : DOWNLEFT}
walls = [b5, b6]

def BounceDown(b):
  """docstring for BounceDown"""
  if b['dir'] == UPLEFT:
    b['dir'] = DOWNLEFT
  if b['dir'] == UPRIGHT:
    b['dir'] = DOWNRIGHT

def BounceUp(b):
  """docstring for BounceUp"""
  if b['dir'] == DOWNLEFT:
    b['dir'] = UPLEFT
  if b['dir'] == DOWNRIGHT:
    b['dir'] = UPRIGHT

def BounceRight(b):
  """docstring for BounceRight"""
  if b['dir'] == DOWNLEFT:
    b['dir'] = DOWNRIGHT
  if b['dir'] == UPLEFT:
    b['dir'] = UPRIGHT

def BounceLeft(b):
  """docstring for BonceLeft"""
  if b['dir'] == DOWNRIGHT:
    b['dir'] = DOWNLEFT
  if b['dir'] == UPRIGHT:
    b['dir'] = UPLEFT

def MoveBlock(b, speed):
  """docstring for MoveBlock"""
  if b['dir'] == DOWNLEFT:
    b['rect'].left -= speed
    b['rect'].top += speed
  if b['dir'] == DOWNRIGHT:
    b['rect'].left += speed
    b['rect'].top += speed
  if b['dir'] == UPLEFT:
    b['rect'].left -= speed
    b['rect'].top -= speed
  if b['dir'] == UPRIGHT:
    b['rect'].left += speed
    b['rect'].top -= speed

def BounceOffWalls(b):
  """docstring for BounceOffWalls"""
  if b['rect'].top < 0:
    # block has moved past the top
    BounceDown(b)
  if b['rect'].bottom > WINDOWHEIGHT:
    # block has moved past the bottom
    BounceUp(b)
  if b['rect'].left < 0:
    # block has moved passed the left side
    BounceRight(b)
  if b['rect'].right > WINDOWWIDTH:
    # block has moved passed the right side
    BounceLeft(b)

def DoesRectTouchVerticalLine(b, vl):
  """docstring for doRectanglesOverlap"""
  if vl.right < b.left or b.right < vl.left:
    return False
  elif vl.top > b.bottom or b.top > vl.bottom:
    return False
  else:
    return True

def DoesRectTouchHorizontalLine(b, hl):
  """docstring for doRectanglesOverlap"""
  if hl.top > b.bottom or b.top > hl.bottom:
    return False
  elif hl.right < b.left or b.right < hl.left:
    return False
  else:
    return True

def BounceOffBlock(b, wall):
  """docstring for BounceOffBlock"""
  br = b['rect']
  w = wall['rect']
  wl = pygame.Rect(w.left, w.top, 1, w.height)
  wr = pygame.Rect(w.right, w.top, 1, w.height)
  wt = pygame.Rect(w.left, w.top, w.width, 1)
  wb = pygame.Rect(w.left, w.bottom, w.width, 1)
  if b['dir'] == UPLEFT:
    if DoesRectTouchVerticalLine(br, wr):
      b['dir'] = UPRIGHT
    elif DoesRectTouchHorizontalLine(br, wb):
      b['dir'] = DOWNLEFT

  if b['dir'] == UPRIGHT:
    if DoesRectTouchVerticalLine(br, wl):
      b['dir'] = UPLEFT
    elif DoesRectTouchHorizontalLine(br, wb):
      b['dir'] = DOWNRIGHT

  if b['dir'] == DOWNLEFT:
    if DoesRectTouchVerticalLine(br, wr):
      b['dir'] = DOWNRIGHT
    elif DoesRectTouchHorizontalLine(br, wt):
      b['dir'] = UPLEFT

  if b['dir'] == DOWNRIGHT:
    if DoesRectTouchVerticalLine(br, wl):
      b['dir'] = DOWNLEFT
    elif DoesRectTouchHorizontalLine(br, wt):
      b['dir'] = UPRIGHT

def BlockIteration(b):
  """BlockIteration moves block one step further,
  bounces it off wals and draws on the surface."""
  MoveBlock(b, MOVESPEED)
  BounceOffWalls(b)
  # Check if blocks overlap with wall
  #[BounceOffBlock(b, w) for w in walls]
  #pygame.draw.rect(windowSurface, b['color'], b['rect'])

def WallIteration(w):
  """BlockIteration moves block one step further,
  bounces it off wals and draws on the surface."""
  MoveBlock(w, 1)
  BounceOffWalls(w)
  pygame.draw.rect(windowSurface, w['color'], w['rect'])

# Run the game loop
while True:
  #Check for the QUIT EVENT
  for event in pygame.event.get():
   if event.type == QUIT:
     pygame.quit()
     sys.exit(0)

  # Draw the black background onto the surface
  windowSurface.fill(BLACK)
  [BlockIteration(b) for b in blocks]
  [WallIteration(w) for w in walls]

  # Draw the window onto the screen
  pygame.display.update()
  time.sleep(0.02)