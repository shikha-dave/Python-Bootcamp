#pir2h
#2pirh+2pir2

class Cylinder:
    pi = 3.14
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return self.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius * (self.radius + self.height)

print(round(Cylinder.volume(Cylinder(2, 3)), 2))
print(round(Cylinder.surface_area(Cylinder(2, 3)), 2))