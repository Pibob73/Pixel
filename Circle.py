from .Letter import Letter


class Circle:
    def __init__(self, center, radius, symbol, area, let=False, danger=False,
                 head=False, color='\033[33m'):
        self.center = center
        self.color = color
        self.radius = radius
        self.symbol = symbol
        self.window = area
        self.head = head
        self.let = let
        self.danger = danger

    def create_circle(self):
        for x in range(self.window.height):
            for y in range(self.window.width):
                aspect = 3
                if ((x - self.center[0])**2) + (y - self.center[1])**2/aspect < self.radius:
                    self.window.create_position(Letter(self.color + self.symbol, head=self.head),
                                                 x, y, danger=self.danger, let=self.let)


