import pygame, sys, time
from pygame.locals import *

class BlockMovement():
  """docstring for BlockMovement"""
  def __init__(self, b):
    self.b = b
    self.dir = b['dir']
  
  def BounceDown(self):
    """docstring for BounceDown"""
    if self.dir == UPLEFT:
      self.dir = DOWNLEFT
    if self.dir == UPRIGHT:
      self.dir = DOWNRIGHT
  
  def BounceUp(self):
    """docstring for BounceUp"""
    if self.dir == DOWNLEFT:
      self.dir = UPLEFT
    if self.dir == DOWNRIGHT:
      self.dir = UPRIGHT

  def BounceRight(self):
    """docstring for BounceRight"""
    if self.dir == DOWNLEFT:
      self.dir = DOWNRIGHT
    if self.dir == UPLEFT:
      self.dir = UPRIGHT

  def BounceLeft(self):
    """docstring for BonceLeft"""
    if self.dir == DOWNRIGHT:
      self.dir = DOWNLEFT
    if self.dir == UPRIGHT:
      self.dir = UPLEFT
  
  def MoveBlock(self, speed):
    """MoveBlock moves the block on the screen"""
    if self.dir == DOWNLEFT:
      self.b['rect'].left -= speed
      self.b['rect'].top += speed
    if self.dir == DOWNRIGHT:
      self.b['rect'].left += speed
      self.b['rect'].top += speed
    if self.dir == UPLEFT:
      self.b['rect'].left -= speed
      self.b['rect'].top -= speed
    if self.dir == UPRIGHT:
      self.b['rect'].left += speed
      self.b['rect'].top -= speed
  
  def BounceOffScreenWalls(self):
    """BounceOffScreenWalls changes the direction of the block and bounces off if the block hits a screen wall"""
    if self.b['rect'].top < 0:
      # block has moved past the top
      Block.BounceDown(self)
    if self.b['rect'].bottom > WINDOWHEIGHT:
      # block has moved past the bottom
      Block.BounceUp(self)
    if self.b['rect'].left < 0:
      # block has moved passed the left side
      Block.BounceRight(self)
    if self.b['rect'].right > WINDOWWIDTH:
      # block has moved passed the right side
      Block.BounceLeft(self)

class Blocks(BlockMovement):
  """docstring for Blocks"""
  def __init__(self, arg):
    BlockMovement.__init__(self, b)
          
  def IsTouchingVerticalLine(self, vl):
    """docstring for IsTouchingVerticalLine"""
    if vl.right < self.b.left or self.b.right < vl.left:
      return False
    elif vl.top > self.b.bottom or self.b.top > vl.bottom:
      return False
    else:
      return True

  def IsTouchingHorizontalLine(self, hl):
    """docstring for IsTouchingHorizontalLine"""
    if hl.top > self.b.bottom or self.b.top > hl.bottom:
      return False
    elif hl.right < self.b.left or self.b.right < hl.left:
      return False
    else:
      return True
  
  def BounceOffBlockWalls(self, wall):
    """BounceOffBlockWalls switches the direction and bounces off the block if it hits a moving block wall"""
    br = b['rect']
    w = wall['rect']
    wl = pygame.Rect(w.left, w.top, 1, w.height)
    wr = pygame.Rect(w.right, w.top, 1, w.height)
    wt = pygame.Rect(w.left, w.top, w.width, 1)
    wb = pygame.Rect(w.left, w.bottom, w.width, 1)
    if self.dir == UPLEFT:
      if IsTouchingVerticalLine(br, wr):
        self.dir = UPRIGHT
      elif IsTouchingHorizontalLine(br, wb):
        self.dir = DOWNLEFT

    if self.dir == UPRIGHT:
      if IsTouchingVerticalLine(br, wl):
        self.dir = UPLEFT
      elif IsTouchingHorizontalLine(br, wb):
        self.dir = DOWNRIGHT

    if self.dir == DOWNLEFT:
      if IsTouchingVerticalLine(br, wr):
        self.dir = DOWNRIGHT
      elif IsTouchingHorizontalLine(br, wt):
        self.dir = UPLEFT

    if self.dir == DOWNRIGHT:
      if IsTouchingVerticalLine(br, wl):
        self.dir = DOWNLEFT
      elif IsTouchingHorizontalLine(br, wt):
        self.dir = UPRIGHT

# class Wall(BlockMovement):
#   """docstring for Wall"""
#   def __init__(self, w):
#     BlockMovement.__init__(self, w)
    
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

# Blocks
b1 = {'rect' : pygame.Rect(300, 80, 55, 60), 'color' : RED, 'dir' : UPRIGHT}
b2 = {'rect' : pygame.Rect(200, 250, 45, 30), 'color' : GREEN, 'dir' : UPLEFT}
b3 = {'rect' : pygame.Rect(100, 150, 67, 60), 'color' : BLUE, 'dir' : DOWNLEFT}
b4 = {'rect' : pygame.Rect(10, 300, 24, 45), 'color' : YELLOW, 'dir' : DOWNRIGHT}
blocks = [b1, b2, b3, b4]
# Wall Blocks
b5 = {'rect' : pygame.Rect(200, 200, 100, 140), 'color' : WHITE, 'dir' : UPRIGHT}
b6 = {'rect' : pygame.Rect(300, 300, 140, 100), 'color' : WHITE, 'dir' : DOWNLEFT}
block_walls = [b5, b6]

def BlockIteration(b):
  """BlockIteration moves block one step further,
  bounces it off walls and draws on the surface."""
  Blocks(BlockMovement.MoveBlock(b, MOVESPEED))
  Blocks(BlockMovement.BounceOffScreenWalls(b))
  # Check if blocks overlap with wall
  [Blocks.BounceOffBlockWalls(b, w) for w in block_walls]
  pygame.draw.rect(windowSurface, b['color'], b['rect'])

def WallIteration(w):
  """WallIteration moves block one step further,
  bounces it off walls and draws on the surface."""
  BlockMovement.MoveBlock(w, 2)
  BlockMovement.BounceOffScreenWalls(w)
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
  [WallIteration(w) for w in block_walls]

  # Draw the window onto the screen
  pygame.display.update()
  time.sleep(0.02)