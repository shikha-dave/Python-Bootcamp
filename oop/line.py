class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1) if self.x2 != self.x1 else float('inf')

line = Line(3, 2, 8, 10)
print(round(line.distance(), 2))
print(round(line.slope(), 2))