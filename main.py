#!/usr/bin/env python3
import os
import time
from Line import Line
from Window import Window
from Block import Block
from Letter import Letter
from Text import Text
from Circle import Circle
from Pixel import Pixel

if __name__ == "__main__":
    heightWindow = 23
    widthWindow = 80
    window = Window()
    Block([0, 0], [22, 79], '#', window, color='\033[35m').create_square()
    Block([5, 5], [17, 74], '█', window, color='\033[36m').create_square()
    Block([2, 3], [16, 73], '█', window, head=True, color='\033[36m').create_square()
    Line('▂', [10, 20], 10, 'right', window, color='\033[32m').create_line()
    Line('*', [6, 3], 17, 'right', window, head=True).create_line()
    Text('I LOVE YOU', [2, 30], window, head=True).print_text()
    Circle([5, 5], 10, '%', window).create_circle()
    Circle([11, 40], 10, '$', window).create_circle()
    Pixel('█', [8, 60], 6, window, '\033[').create_pixel()
    window.create_position(Letter('*', color='\033[33m', head=True), 2, 29)
    window.create_position(Letter('*', color='\033[33m', head=True), 2, 40)
    window.create_position(Letter('♚', color='\033[37m'), 9, 8)
    window.create_position(Letter('@', color='\033[32m'), 9, 30)
    exitProgramme = False
    while not exitProgramme:
        if window.action:
            os.system("clear")
            window.print_window()
            window.action = False
        time.sleep(2)


