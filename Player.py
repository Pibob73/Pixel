class Player:
    def __init__(self):
        self.life = True
        self.heart = 5
        self.bag = ['/']
        self.effect = []
        self.direction = ''

    def move_player(self, direction):
        if direction == 'w':
            self.direction = 'up'
        if direction == 'a':
            self.direction = 'left'
        if direction == 'd':
            self.direction = 'right'
        if direction == 's':
            self.direction = 'down'
        if direction == '.':
            self.direction = ''
