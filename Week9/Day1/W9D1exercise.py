class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color) # red
print(Circle.color) # red
print(circle1.get_color()) # red
circle1.grow(3)
print(circle1.diameter) # 6