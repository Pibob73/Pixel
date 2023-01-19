from Letter import Letter
from Empty import Empty
from UnitABC import UnitABC


class Window:
    #23 80
    height = 23
    width = 80
    action = True

    def __init__(self):
        self.cells = []
        for i in range(self.height):
            self.cells.append([Empty()] * self.width)

    def create_position(self, letter, row, column):
        maybe_empty = self.cells[row][column]
        if maybe_empty.superimposer() or letter.head:
            self.cells[row][column] = letter
        else:
            return False

    def print_window(self):
        for row in self.cells:
            for cell in row:
                print(cell.symbol, end='')
            print()

    def clear_window(self):
        self.cells = []
        for i in range(self.height):
            self.cells.append([Empty()] * self.width)

