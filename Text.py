from Window import Window
from Letter import Letter


class Text:
    def __init__(self, text, begin, area, head=False, color='\033[37m'):
        self.text = text
        self.color = color
        self.begin = begin
        self.length = len(text)
        self.direction = 'right'
        self.window = area
        self.head = head

    def print_text(self):
        print(self.head)
        for letter in range(self.length):
            if self.text[letter] == ' ':
                continue
            self.window.create_position(Letter(self.color + self.text[letter], head=self.head),
                                        self.begin[0], self.begin[1] + letter)
