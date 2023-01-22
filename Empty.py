from .UnitABC import UnitABC


class Empty(UnitABC):
    symbol = ' '
    back_object = True
    head = False
    def __init__(self, head=False):
        self.head = head

    def superimposer(self):
        return self.back_object

