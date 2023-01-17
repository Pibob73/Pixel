from UnitABC import UnitABC


class Empty(UnitABC):
    symbol = ' '
    backObject = True
    head = False

    def superimposer(self):
        return self.backObject

