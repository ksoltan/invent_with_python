b1 = {'rect' : pygame.Rect(300, 80, 55, 60), 'color' : RED, 'dir' : UPRIGHT}
b2 = {'rect' : pygame.Rect(200, 250, 45, 30), 'color' : GREEN, 'dir' : UPLEFT}
b3 = {'rect' : pygame.Rect(100, 150, 67, 60), 'color' : BLUE, 'dir' : DOWNLEFT}
b4 = {'rect' : pygame.Rect(10, 300, 24, 45), 'color' : YELLOW, 'dir' : DOWNRIGHT}
blocks = [b1, b2, b3, b4]

# White wall-like block
b5 = {'rect' : pygame.Rect(250, 340, 200, 10), 'color' : WHITE}
wallBottom = b5['rect'].bottom
wallTop = b5['rect'].top
wallLeft = b5['rect'].left
wallRight = b5['rect'].right

for b in blocks:
  # If point on the top or bottom corresponds to wall
  for r_b in range(b['rect'].left, b['rect'].right):
    for c_b in range(b['rect'].top, b['rect'].bottom):
       for r_w in range(wallLeft, wallRight):
         for c_w in range(wallTop, wallBottom):
           if [r_b, c_b] == [r_w, c_w]:
             