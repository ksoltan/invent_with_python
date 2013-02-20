import pygame, sys, random, time
from pygame.locals import *

def BounceDown(b):
  """docstring for BounceDown"""
  if b['dir'] == UPLEFT:
    b['dir'] = DOWNLEFT
  if b['dir'] == UPRIGHT:
    b['dir'] = DOWNRIGHT
  if b['dir'] == UP:
    b['dir'] = DOWN

def BounceUp(b):
  """docstring for BounceUp"""
  if b['dir'] == DOWNLEFT:
    b['dir'] = UPLEFT
  if b['dir'] == DOWNRIGHT:
    b['dir'] = UPRIGHT
  if b['dir'] == DOWN:
    b['dir'] = UP

def BounceRight(b):
  """docstring for BounceRight"""
  if b['dir'] == DOWNLEFT:
    b['dir'] = DOWNRIGHT
  if b['dir'] == UPLEFT:
    b['dir'] = UPRIGHT
  if b['dir'] == LEFT:
    b['dir'] = RIGHT

def BounceLeft(b):
  """docstring for BonceLeft"""
  if b['dir'] == DOWNRIGHT:
    b['dir'] = DOWNLEFT
  if b['dir'] == UPRIGHT:
    b['dir'] = UPLEFT
  if b['dir'] == RIGHT:
    b['dir'] = LEFT

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
  if b['dir'] == UP:
    b['rect'].top -= speed
  if b['dir'] == DOWN:
    b['rect'].top += speed
  if b['dir'] == RIGHT:
    b['rect'].left += speed
  if b['dir'] == LEFT:
    b['rect'].left -= speed

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

def BlockIteration(b, walls):
  """BlockIteration moves block one step further,
  bounces it off wals and draws on the surface."""
  MoveBlock(b, MOVESPEED)
  BounceOffWalls(b)
  [BounceOffBlock(b, w) for w in walls]

def WallIteration(w):
  """BlockIteration moves block one step further,
  bounces it off wals and draws on the surface."""
  MoveBlock(w, EVILSPEED)
  BounceOffWalls(w)

def MovePlayerLeft():
  """docstring for MovePlayerLeft"""
  moveRight = False
  moveLeft = True
def MovePlayerRight():
  """docstring for MovePlayerRight"""
  moveRight = True
  moveLeft = False

def MovePlayerUp():
  """docstring for MovePlayerUp"""
  moveDown = False
  moveUp = True

def MovePlayerDown():
  """docstring for MovePlayerDown"""
  moveDown = True
  moveUp = False

def MovePlayer():
  if moveDown and player.bottom < WINDOWHEIGHT:
    player.top += MOVESPEED
  elif moveUp and player.top > 0:
    player.top -= MOVESPEED
  elif moveLeft and player.left > 0:
    player.left -= MOVESPEED
  elif moveRight and player.right < WINDOWWIDTH:
    player.right += MOVESPEED

pygame.init()

# Set up the window
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Food and Evil')
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
FOODNUMBER = 40
FOODEATEN = 0
foodCounter = 0
FOODSIZE = 20
food_blocks = []
for i in range(FOODNUMBER):
  food_blocks.append({'rect' : pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE + 10), 'dir' : direction[random.randint(0, 3)]})

# Evil red block
evil1 = {'rect': pygame.Rect(100, 40, 40, 50), 'dir' : UPRIGHT}
evil2 = {'rect': pygame.Rect(50, 400, 40, 50), 'dir' : UPLEFT}
evil3 = {'rect': pygame.Rect(100, 37, 40, 50), 'dir' : DOWNLEFT}
evil4 = {'rect': pygame.Rect(15, 490, 40, 50), 'dir' : DOWNRIGHT}
evil5 = {'rect': pygame.Rect(100, 30, 40, 50), 'dir' : RIGHT}
evil6 = {'rect': pygame.Rect(200, 490, 40, 50), 'dir' : DOWN}
evil_blocks = [evil1, evil2, evil3, evil4, evil5, evil6]

# Player
player = pygame.Rect(300, 100, 50, 50)
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
EVILSPEED = 4

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
  windowSurface.fill(BLACK)
  [WallIteration(e) for e in evil_blocks]
  [pygame.draw.rect(windowSurface, RED, e['rect']) for e in evil_blocks]
  MovePlayer(moveDown, moveUp, moveRight, moveLeft)
  #pygame.draw.rect(windowSurface, WHITE, player)
  windowSurface.blit(current_player_image, player)
  if not food_blocks:
    windowSurface.blit(win_text, win_textRect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit(0)
  # if len(food_blocks) < 40:
  #   for i in range(5):
  #     food_blocks.append({'rect' : pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE + 10), 'dir' : direction[random.randint(0, 3)]})
  for f in food_blocks:
    BlockIteration(f, evil_blocks)
# Check if player intersected with food
  for f in food_blocks[:]:
    if player.colliderect(f['rect']):
      food_blocks.remove(f)
      FOODEATEN += 1
      pickUpSound.play()
      windowSurface.blit(playerStretchedImageBite, player)        
  food_text = basicFont.render('{0}'.format(FOODEATEN), True, WHITE)
  food_textRect = food_text.get_rect()
  windowSurface.blit(food_text, food_textRect)
  for e in evil_blocks:
    if player.colliderect(e['rect']):
      windowSurface.blit(lose_text, lose_textRect)
      pygame.display.update()
      time.sleep(2)
      pygame.quit()
      sys.exit(0)
  # Draw food
  for f in food_blocks:
    pygame.draw.rect(windowSurface, GREEN, f['rect'])

  pygame.display.update()
  mainClock.tick(40)