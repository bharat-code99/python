class Cylinder:

    def __init__(self, height: int = 1, radius: int = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)


cy = Cylinder(2, 3)
print(f"Volume of cylinder: {cy.volume()}")
print(f"Surface area of cylinder: {cy.surface_area()}")


class Line:
    def __init__(self, coor1:tuple[int, int], coor2:tuple[int, int]):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2) ** 0.5

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3,2)
coordinate2 = (8,10)

# ln = Line(coordinate1,coordinate2)
# print(ln.distance())
# print(ln.slope())