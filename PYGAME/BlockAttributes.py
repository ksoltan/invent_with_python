# Common block actions for PYGAME

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 2

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

def BlockIteration(b, walls):
  """BlockIteration moves block one step further,
  bounces it off wals and draws on the surface."""
  MoveBlock(b, MOVESPEED)
  BounceOffWalls(b)
  [BounceOffBlock(b, w) for w in walls]
  #pygame.draw.rect(windowSurface, b['color'], b['rect'])

def WallIteration(w):
  """BlockIteration moves block one step further,
  bounces it off wals and draws on the surface."""
  MoveBlock(w, 1)
  BounceOffWalls(w)
  #pygame.draw.rect(windowSurface, w['color'], w['rect'])