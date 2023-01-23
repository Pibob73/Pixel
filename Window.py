from .Empty import Empty
import random
class Window:
    #23 80
    def __init__(self, height=23, width=80):
        self.height = height
        self.width = width
        self.action = True
        self.cells = []
        self.let = []
        self.danger = []
        for i in range(self.height):
            self.cells.append([Empty()] * self.width)
        for i in range(self.height):
            self.let.append([False] * self.width)
        for i in range(self.height):
            self.danger.append([False] * self.width)


    def create_position(self, letter, row, column, let=False, danger=False):
        maybe_empty = self.cells[row][column]
        if maybe_empty.superimposer() or letter.head:
            self.cells[row][column] = letter
            if let:
                self.let[row][column] = True
            if danger:
                self.danger[row][column] = True
        else:
            return False

    def print_window(self):
        for row in self.cells:
            for cell in row:
                print(cell.symbol, end='')
            print()

    def clear_window(self):
        self.cells = []
        self.danger = []
        for i in range(self.height):
            self.cells.append([Empty()] * self.width)
        for i in range(self.height):
            self.danger.append([False] * self.width)

