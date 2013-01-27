# There are thirty lights in a row. Thirty frogs jump across them.
# The first frog lands on every single light. The second frog lands on every
# other light. The third frog lands on every third light, and so on. When a
# frog lands on a light, it turns on if it was off, and off if it was on. If
# all the lights are off to begin with, how many are on after the last frog
# has jumped?

def main():
  lights = []
  for l in range(1, 31):
    lights.append(False)
  
  for f in range(1, 31):
    print 'Frog:', f
    for i in range(1, 31):
      if i%f == 0:
        lights[i-1] = not lights[i-1]
    print 'Lights:', lights
    
  lights_on = 0
  for l in lights:
    if l:
      lights_on += 1
  print 'Lights on:', lights_on

if __name__ == '__main__':
  main()
