# Practicing classes:
# Variables are calles Attributes
# Functions inside class called Methods
class Shape:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  description = 'This shape has not been described yet'
  author = 'Nobody has claimed to make this shape yet'
  def area(self):
    return self.length * self.width
  def perimeter(self):
    return 2 * self.length + 2 * self.width
  def describe(self, text):
    self.description = text
  def authorName(self, text):
    self.author = text
  def scaleSize(self, scale):
    self.length = self.length * scale
    self.width = self.width * scale

rectangle = Shape(100, 45)
# Get area of rectangle:
print rectangle.area()
# Get perimeter of rectangle:
print rectangle.perimeter()
# Describing rectangle:
rectangle.describe('A wide rectangle, more than twice\
as wide as it is tall')
# Making the rectangle 50% of its size:
rectangle.scaleSize(0.5)
# Reprinting area of rectangle:
rectangle.area()

# Create new instance:
long_rectangle = Shape(200, 20)
fatrectangle = Shape(130, 120)

# Inheritance, adding attribute to a basic design:
class Square(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = length