import pygame, sys, random, time
from pygame.locals import *

def doRectsOverlap(rect1, rect2):
  """docstring for doRectanglesOverlap"""
  for a, b in [(rect1, rect2), (rect2, rect1)]:
    # Check if a's corners are inside b
    if ((isPointInsideRect(a.left, a.top, b)) or (isPointInsideRect(a.left, a.bottom, b)) or (isPointInsideRect(a.right, a.top, b)) or (isPointInsideRect(a.right, a.bottom, b))):
      return True
  return False

def isPointInsideRect(x, y, rect):
  if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
    return True
  else:
    return False

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 5

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# set up the bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
bouncer = {'rect' : pygame.Rect(300, 100, 50, 35), 'dir' : UPLEFT}
# Counter on the bouncer of how many food pieces were eaten
FOODEATEN = 0
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('{0}'.format(FOODEATEN), True, WHITE)
textRect = text.get_rect()
foods = []
for i in range(20):
  foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

while True:
  # check for QUIT event
  for event in pygame.event.get():
   if event.type == QUIT:
     pygame.quit()
     sys.exit(0)
  foodCounter += 1
  if foodCounter >= NEWFOOD:
    # add new food
    foodCounter = 0
    foods.append(pygame.Rect(random.randint(10, WINDOWWIDTH - FOODSIZE), random.randint(10, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
  
  # draw the black background onto the surface
  windowSurface.fill(BLACK)
  
  # move the bouncer data structure
  if bouncer['dir'] == DOWNLEFT:
    bouncer['rect'].left -= MOVESPEED
    bouncer['rect'].top += MOVESPEED
  if bouncer['dir'] == DOWNRIGHT:
    bouncer['rect'].left += MOVESPEED
    bouncer['rect'].top += MOVESPEED
  if bouncer['dir'] == UPLEFT:
    bouncer['rect'].left -= MOVESPEED
    bouncer['rect'].top -= MOVESPEED
  if bouncer['dir'] == UPRIGHT:
    bouncer['rect'].left += MOVESPEED
    bouncer['rect'].top -= MOVESPEED
  
  # Check if the bouncer has move out of the window
  if bouncer['rect'].top < 0:
    # block has moved past the top
    if bouncer['dir'] == UPLEFT:
      bouncer['dir'] = DOWNLEFT
    if bouncer['dir'] == UPRIGHT:
      bouncer['dir'] = DOWNRIGHT
  if bouncer['rect'].bottom > WINDOWHEIGHT:
    # block has moved past the bottom
    if bouncer['dir'] == DOWNLEFT:
      bouncer['dir'] = UPLEFT
    if bouncer['dir'] == DOWNRIGHT:
      bouncer['dir'] = UPRIGHT
  if bouncer['rect'].left < 0:
    # block has moved passed the left side
    if bouncer['dir'] == DOWNLEFT:
      bouncer['dir'] = DOWNRIGHT
    if bouncer['dir'] == UPLEFT:
      bouncer['dir'] = UPRIGHT
  if bouncer['rect'].right > WINDOWWIDTH:
    # block has moved passed the right side
    if bouncer['dir'] == DOWNRIGHT:
      bouncer['dir'] = DOWNLEFT
    if bouncer['dir'] == UPRIGHT:
      bouncer['dir'] = UPLEFT
  # draw the bouncer onto the surface
  pygame.draw.rect(windowSurface, WHITE, bouncer['rect'])
  # check if the bouncer has intersected with any food squares
  for food in foods[:]:
    if doRectsOverlap(bouncer['rect'], food):
      foods.remove(food)
      FOODEATEN += 1
  basicFont = pygame.font.SysFont(None, 48)
  text = basicFont.render('{0}'.format(FOODEATEN), True, WHITE)
  textRect = text.get_rect()
  windowSurface.blit(text, textRect)
  # draw the food
  for i in range(len(foods)):
    pygame.draw.rect(windowSurface, GREEN, foods[i])
  # draw the window onto the screen
  pygame.display.update()
  mainClock.tick(40)
  time.sleep(0.05)