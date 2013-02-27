import math
import pygame
import sys
import time
from pygame.locals import *

WINDOWWIDTH = 500
WINDOWHEIGHT = 500

# Set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
RIGHT = 6
LEFT = 4

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Block():
  """Describes one moving block in a window."""
  def __init__(self, rect, color, direction):
    # super(Block, self).__init__()
    self.rect = rect
    self.color = color
    self.dir = direction

  def BounceDown(self):
    """Bounces this block down (flips vertical direction down).
    
    Does nothing if block already moves down. If block is moving
    up - flips vertical composite down, so up-left turns into
    down-left and up-right turns into down right.
    """
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
    """docstring for MoveBlock"""
    if self.dir == DOWNLEFT:
      self.rect.left -= speed
      self.rect.top += speed
    if self.dir == DOWNRIGHT:
      self.rect.left += speed
      self.rect.top += speed
    if self.dir == UPLEFT:
      self.rect.left -= speed
      self.rect.top -= speed
    if self.dir == UPRIGHT:
      self.rect.left += speed
      self.rect.top -= speed

  def BounceOffWalls(self):
    """docstring for BounceOffWalls"""
    if self.rect.top < 0:
      # block has moved past the top
      self.BounceDown()
    if self.rect.bottom > WINDOWHEIGHT:
      # block has moved past the bottom
      self.BounceUp()
    if self.rect.left < 0:
      # block has moved passed the left side
      self.BounceRight()
    if self.rect.right > WINDOWWIDTH:
      # block has moved passed the right side
      self.BounceLeft()

  def DoesRectTouchVerticalLine(self, vl):
    """docstring for doRectanglesOverlap"""
    b = self.rect
    if vl.right < b.left or b.right < vl.left:
      return False
    elif vl.top > b.bottom or b.top > vl.bottom:
      return False
    else:
      return True

  def DoesRectTouchHorizontalLine(self, hl):
    """docstring for doRectanglesOverlap"""
    b = self.rect
    if hl.top > b.bottom or b.top > hl.bottom:
      return False
    elif hl.right < b.left or b.right < hl.left:
      return False
    else:
      return True

  def BounceOffBlock(self, wall):
    """docstring for BounceOffBlock"""
    br = self.rect
    w = wall.rect
    wl = pygame.Rect(w.left, w.top, 1, w.height)
    wr = pygame.Rect(w.right, w.top, 1, w.height)
    wt = pygame.Rect(w.left, w.top, w.width, 1)
    wb = pygame.Rect(w.left, w.bottom, w.width, 1)
    if self.dir == UPLEFT:
      if self.DoesRectTouchVerticalLine(wr):
        self.dir = UPRIGHT
      elif self.DoesRectTouchHorizontalLine(wb):
        self.dir = DOWNLEFT

    if self.dir == UPRIGHT:
      if self.DoesRectTouchVerticalLine(wl):
        self.dir = UPLEFT
      elif self.DoesRectTouchHorizontalLine(wb):
        self.dir = DOWNRIGHT

    if self.dir == DOWNLEFT:
      if self.DoesRectTouchVerticalLine(wr):
        self.dir = DOWNRIGHT
      elif self.DoesRectTouchHorizontalLine(wt):
        self.dir = UPLEFT

    if self.dir == DOWNRIGHT:
      if self.DoesRectTouchVerticalLine(wl):
        self.dir = DOWNLEFT
      elif self.DoesRectTouchHorizontalLine(wt):
        self.dir = UPRIGHT

  def BlockIteration(self, windowSurface, movespeed, walls):
    """BlockIteration moves block one step further,
    bounces it off wals and draws on the surface."""
    self.MoveBlock(movespeed)
    self.BounceOffWalls()
    # Check if blocks overlap with wall
    [self.BounceOffBlock(w) for w in walls]
    pygame.draw.rect(windowSurface, self.color, self.rect)

  def WallIteration(self, windowSurface, movespeed):
    """BlockIteration moves block one step further,
    bounces it off wals and draws on the surface."""
    self.MoveBlock(movespeed)
    self.BounceOffWalls()
    pygame.draw.rect(windowSurface, self.color, self.rect)

class Game():
  """docstring for Game"""
  def __init__(self, level_duration):
    # super(Game, self).__init__()
    self.InitLevelTracking(level_duration)

    # Set up the block data structure
    b1 = Block(pygame.Rect(300, 80, 55, 60), RED, UPRIGHT)
    b2 = Block(pygame.Rect(200, 250, 45, 30), GREEN, UPLEFT)
    b3 = Block(pygame.Rect(100, 150, 67, 60), BLUE, DOWNLEFT)
    b4 = Block(pygame.Rect(10, 300, 24, 45), YELLOW, DOWNRIGHT)
    self.blocks = [b1, b2, b3, b4]

    # White wall-like block
    b5 = Block(pygame.Rect(200, 200, 100, 140), WHITE, UPRIGHT)
    b6 = Block(pygame.Rect(300, 300, 140, 100), WHITE, DOWNLEFT)
    self.walls = [b5, b6]

  def Iteration(self, windowSurface):
    """docstring for Iteration"""
    # Draw the black background onto the surface
    windowSurface.fill(BLACK)

    # Iterate all the blocks
    [b.BlockIteration(
        windowSurface, self.speed, self.walls) for b in self.blocks]
    [w.WallIteration(windowSurface, self.speed) for w in self.walls]

    # Check if we should bump the level.
    self.CheckIfLevelIsComplete()

  def InitLevelTracking(self, level_duration):
    self.level_duration = level_duration
    self.level = 0
    self.level_end_time = time.time() + level_duration
    self.BumpLevel()

  def CheckIfLevelIsComplete(self):
    """docstring for fname"""
    # Check if we should bump the level.
    if self.level_end_time < time.time():
      self.BumpLevel()
      self.level_end_time = time.time() + self.level_duration

  def BumpLevel(self):
    """docstring for SetLevel"""
    self.level += 1
    self.speed = math.log1p(self.level)
    print "New speed", self.speed

def main():
  """docstring for main"""
  # Set up pygame
  pygame.init()
  # Set up the window
  windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
  pygame.display.set_caption('Animation')

  # Run the game loop
  game = Game(5)  # each level lasts 5 seconds 
  while True:
    #Check for the QUIT EVENT
    for event in pygame.event.get():
     if event.type == QUIT:
       pygame.quit()
       sys.exit(0)

    # Draw the black background onto the surface
    game.Iteration(windowSurface)

    # Draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)

if __name__ == '__main__':
    main()
