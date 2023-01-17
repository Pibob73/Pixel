from UnitABC import UnitABC


class Letter(UnitABC):
    head = False

    def __init__(self, symbol=' ', color='', head=False):
        self.symbol = color + symbol
        self.color = color
        self.backObject = False
        self.static = True
        self.head = head

    def superimposer(self):
        return self.backObject
