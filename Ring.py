from .Letter import Letter

class Ring:
    def __init__(self, center, radius, symbol, area, danger=False, let=False,
                 head=False, color='\033[33m'):
        self.center = center
        self.color = color
        self.radius = radius
        self.symbol = symbol
        self.window = area
        self.head = head
        self.danger = danger
        self.let = let

    def create_circle(self):
        for x in range(self.window.height):
            for y in range(self.window.width):
                aspect = 3
                attitude = ((x - self.center[0])**2) + (y - self.center[1])**2/aspect
                if attitude < self.radius and attitude > self.radius - 6:
                    self.window.create_position(Letter(self.color + self.symbol, head=self.head),
                                                x, y, danger=self.danger, let=self.let,)

