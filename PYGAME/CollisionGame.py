import pygame, sys, random, time
from pygame.locals import *

class Block():
  """docstring for Block"""
  def __init__(self, rect, direction):
    #super(Block, self).__init__()
    self.rect = rect
    self.dir = direction
    
  def BounceDown(self):
    """docstring for BounceDown"""
    if self.dir == UPLEFT:
      self.dir = DOWNLEFT
    if self.dir == UPRIGHT:
      self.dir = DOWNRIGHT
    if self.dir == UP:
      self.dir = DOWN

  def BounceUp(self):
    """docstring for BounceUp"""
    if self.dir == DOWNLEFT:
      self.dir = UPLEFT
    if self.dir == DOWNRIGHT:
      self.dir = UPRIGHT
    if self.dir == DOWN:
      self.dir = UP

  def BounceRight(self):
    """docstring for BounceRight"""
    if self.dir == DOWNLEFT:
      self.dir = DOWNRIGHT
    if self.dir == UPLEFT:
      self.dir = UPRIGHT
    if self.dir == LEFT:
      self.dir = RIGHT

  def BounceLeft(self):
    """docstring for BonceLeft"""
    if self.dir == DOWNRIGHT:
      self.dir = DOWNLEFT
    if self.dir == UPRIGHT:
      self.dir = UPLEFT
    if self.dir == RIGHT:
      self.dir = LEFT

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
    if self.dir == UP:
      self.rect.top -= speed
    if self.dir == DOWN:
      self.rect.top += speed
    if self.dir == RIGHT:
      self.rect.left += speed
    if self.dir == LEFT:
      self.rect.left -= speed

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

  def BlockIteration(self, walls):
    """BlockIteration moves block one step further,
    bounces it off wals and draws on the surface."""
    self.MoveBlock(MOVESPEED)
    self.BounceOffWalls()
    [self.BounceOffBlock(w) for w in walls]
    pygame.draw.rect(windowSurface, GREEN, self.rect)
    
  def WallIteration(self):
    """BlockIteration moves block one step further,
    bounces it off wals and draws on the surface."""
    self.MoveBlock(EVILSPEED)
    self.BounceOffWalls()
    pygame.draw.rect(windowSurface, RED, self.rect)

class Player():
  """docstring for Player"""
  def __init__(self, player):
    #super(Player, self).__init__()
    self.player = player
    
  def MovePlayerLeft(self):
    """docstring for MovePlayerLeft"""
    moveRight = False
    moveLeft = True
  def MovePlayerRight(self):
    """docstring for MovePlayerRight"""
    moveRight = True
    moveLeft = False

  def MovePlayerUp(self):
    """docstring for MovePlayerUp"""
    moveDown = False
    moveUp = True

  def MovePlayerDown(self):
    """docstring for MovePlayerDown"""
    moveDown = True
    moveUp = False

  def PlayerMove(self, windowSurface):
    if moveDown and self.player.bottom < WINDOWHEIGHT:
      self.player.top += MOVESPEED
    elif moveUp and self.player.top > 0:
      self.player.top -= MOVESPEED
    elif moveLeft and self.player.left > 0:
      self.player.left -= MOVESPEED
    elif moveRight and self.player.right < WINDOWWIDTH:
      self.player.right += MOVESPEED
    windowSurface.blit(current_player_image, self.player)

def AddMoreFood():
  if len(food_blocks) < 40:
    for i in range(5):
      food_blocks.append({'rect' : pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE + 10), 'dir' : direction[random.randint(0, 3)]})

def GameIteration():
  windowSurface.fill(BLACK)
  [e.WallIteration() for e in evil_blocks]
  player.PlayerMove(windowSurface)
  IfAllFoodEaten()
  [f.BlockIteration(evil_blocks) for f in food_blocks[:]]
  PickUpFood()
  DrawFoodNumber()
  IfCollidesWithEvil()
  pygame.display.update()
  mainClock.tick(40)
  
def IfCollidesWithEvil():
  '''If the player bumps into evil red block, the game is lost.'''
  for e in evil_blocks:
    if player.player.colliderect(e.rect):
      windowSurface.blit(lose_text, lose_textRect)
      pygame.display.update()
      time.sleep(2)
      pygame.quit()
      sys.exit(0)

def IfAllFoodEaten():
  '''If all food is eaten, the game is won.'''
  if not food_blocks:
    windowSurface.blit(win_text, win_textRect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit(0)
  
def PickUpFood():
  global FOODEATEN
  for f in food_blocks[:]:
    if player.player.colliderect(f.rect):
      food_blocks.remove(f)
      FOODEATEN += 1
      pickUpSound.play()
      windowSurface.blit(playerStretchedImageBite, player.player)

def DrawFoodNumber():
  food_text = basicFont.render('{0}'.format(FOODNUMBER - len(food_blocks)), True, WHITE)
  food_textRect = food_text.get_rect()
  windowSurface.blit(food_text, food_textRect)

pygame.init()
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Food and Evil: LEVEL 1')
LEVEL = 1
mainClock = pygame.time.Clock()

# Direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
DOWN = 2
UP = 8
RIGHT = 6
LEFT = 4
direction = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Music
pickUpSound = pygame.mixer.Sound('gulp.wav')
pygame.mixer.music.load('chase.wav')
pygame.mixer.music.play(-1, 0.0)

# Food Data structure
FOODNUMBER = 50
FOODEATEN = 0
FOODSIZE = 20
food_blocks = []
for i in range(FOODNUMBER):
  food_blocks.append(Block(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE + 10), direction[random.randint(0, 3)]))

# Evil red block
evil1 = Block(pygame.Rect(100, 40, 40, 50), UPRIGHT)
evil2 = Block(pygame.Rect(50, 400, 40, 50), UPLEFT)
evil3 = Block(pygame.Rect(100, 37, 40, 50), DOWNLEFT)
evil4 = Block(pygame.Rect(15, 490, 40, 50), DOWNRIGHT)
evil5 = Block(pygame.Rect(100, 30, 40, 50), RIGHT)
evil6 = Block(pygame.Rect(200, 490, 40, 50), DOWNRIGHT)
evil_blocks = [evil1, evil2, evil3, evil4, evil5, evil6]

# Player
player = Player(pygame.Rect(300, 100, 50, 50))
playerImage = pygame.image.load('yellowcircle2.png')
playerImageBite = pygame.image.load('yellowbitecircle2.png')
playerStretchedImage = pygame.transform.scale(playerImage, (50, 50))
playerStretchedImageBite = pygame.transform.scale(playerImageBite, (50, 50))
playerBiteRight = playerStretchedImageBite
playerBiteUp = pygame.transform.rotate(playerBiteRight, 90)
playerBiteLeft = pygame.transform.rotate(playerBiteUp, 90)
playerBiteDown = pygame.transform.rotate(playerBiteLeft, 90)

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
current_player_image = playerBiteRight
 
MOVESPEED = 5
EVILSPEED = 5

# Text
basicFont = pygame.font.SysFont(None, 48)
win_text = basicFont.render('YOU WIN!', True, WHITE)
win_textRect = win_text.get_rect()
win_textRect.centerx = windowSurface.get_rect().centerx
win_textRect.centery = windowSurface.get_rect().centery
lose_text = basicFont.render('YOU LOSE!', True, RED)
lose_textRect = lose_text.get_rect()
lose_textRect.centerx = windowSurface.get_rect().centerx
lose_textRect.centery = windowSurface.get_rect().centery

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)
    if event.type == KEYDOWN:
      # Change the keyboard variables
      if event.key == K_LEFT or event.key == ord('a'):
        moveRight = False
        moveLeft = True
        current_player_image = playerBiteLeft
      if event.key == K_RIGHT or event.key == ord('d'):
        moveRight = True
        moveLeft = False
        current_player_image = playerBiteRight
      if event.key == K_UP or event.key == ord('w'):
        moveDown = False
        moveUp = True
        current_player_image = playerBiteUp
      if event.key == K_DOWN or event.key == ord('s'):
        moveDown = True
        moveUp = False
        current_player_image = playerBiteDown
    if event.type == KEYUP:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit(0)
      if event.key == K_LEFT or event.key == ord('a'):
        moveLeft = False
      if event.key == K_RIGHT or event.key == ord('d'):
        moveRight = False
      if event.key == K_UP or event.key == ord('w'):
        moveUp = False
      if event.key == K_DOWN or event.key == ord('s'):
          moveDown = False
  GameIteration()