class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.circumference = round(2 * Circle.pi * radius, 2)

    def get_area(self):
        return Circle.pi * self.radius ** 2


circle1 = Circle(5)
print(circle1.circumference)
print(circle1.get_area())