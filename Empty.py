from UnitABC import UnitABC


class Empty(UnitABC):
    symbol = ' '
    back_object = True
    head = False

    def superimposer(self):
        return self.back_object

