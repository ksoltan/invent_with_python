import copy
import math

# Practicing classes:
# Variables are calles Attributes
# Functions inside class called Methods
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "Point({0},{1})".format(self.x, self.y)
    
  def translate(self, direction):
    return Point(self.x + direction.dx, self.y + direction.dy)

class Vector:
  def __init__(self, dx, dy):
    self.dx = dx
    self.dy = dy

  def __str__(self):
    return "Vector({0},{1})".format(self.dx, self.dy)

  def translate(self, direction):
    return Vector(self.dx + direction.dx, self.dy + direction.dy)

  def scale(self, scale):
    return Vector(self.dx * scale, self.dy * scale)

class Size:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    
  def __str__(self):
    return "Size({0},{1})".format(self.w, self.h)

  def scale(self, scale):
    return Size(self.w * scale, self.h * scale)
    

class Shape2D:
  """docstring for Shape"""
  def __init__(self, origin):
    self.origin = origin

  def area(self):
    raise Exception('Must override in child class!')

  def perimeter(self):
    raise Exception('Must override in child class!')

  def moveTo(self, new_origin):
    """docstring for fname"""
    self.origin = new_origin

class Rectangle(Shape2D):
  def __init__(self, origin, size):
    Shape2D.__init__(self, origin)
    self.size = size

  def __str__(self):
    return "Rectange({0},{1})".format(str(self.origin), str(self.size))

  def area(self):
    return self.size.w * self.size.h

  def perimeter(self):
    return 2 * (self.size.w + self.size.h)

  def scale(self, scale):
    return Rectangle(copy.copy(self.origin), self.size.scale(scale))
    
  def translate(self, direction):
    return Rectangle(self.origin.translate(direction), copy.copy(self.size))

class Circle(Shape2D):
  def __init__(self, origin, radius):
    Shape2D.__init__(self, origin)
    self.radius = radius

  def __str__(self):
    return "Circle({0},{1})".format(str(self.origin), self.radius)

  def area(self):
    return math.pi * self.radius**2

  def perimeter(self):
    return 2 * math.pi * self.radius

  def scale(self, scale):
    return Circle(copy.copy(self.origin), self.radius * 2)

  def translate(self, direction):
    return Circle(self.origin.translate(direction), self.radius)
