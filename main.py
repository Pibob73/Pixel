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
from Fill import Fill
from Drone import Drone
def pattern():
    Block([0, 0], [22, 79], '#', window, color='\033[35m').create_block()
    Block([5, 5], [17, 74], '█', window, color='\033[36m').create_block()
    Block([2, 3], [16, 73], '█', window, head=True, floor=True, color='\033[36m').create_block()
    Circle([11, 40], 10, '$', window, head=True).create_circle()
    Line('▂', [10, 20], 30, 'right', window, head=True, color='\033[32m').create_line()
    Line('*', [6, 3], 17, 'right', window, head=True).create_line()
    Text('I LOVE YOU', [2, 30], window, head=True).print_text()
    Text('CAR ||', [5, 30], window, head=True).print_text()
    Circle([5, 5], 10, '%', window).create_circle()
    Circle([13, 8], 5, '%', window, color='\033[32m').create_circle()
    window.create_position(Letter('0', color='\033[33m', head=True), 13, 8)
    window.create_position(Letter('a', color='\033[31m', head=True), 14, 10)
    window.create_position(Letter('a', color='\033[31m', head=True), 12, 7)
    Pixel('=', [8, 60], 6, window, color='\033[31m', floor=True).create_pixel()
    window.create_position(Letter('*', color='\033[33m', head=True), 2, 29)
    window.create_position(Letter('*', color='\033[33m', head=True), 2, 40)
    window.create_position(Letter('♚', color='\033[37m'), 9, 8)


if __name__ == "__main__":
    heightWindow = 23
    widthWindow = 80
    window = Window()
    exitProgramme = False
    drone = Drone([8, 30], '@', window)
    drone.create_drone()
    while not exitProgramme:
        pattern()
        Block([6, 4], [10, 10], '*', window, color='\033[36m', floor=True).create_block()
        if window.action or True:
            os.system("clear")
            Fill([1, 1], ',', window, color='\033[32m').fill()
            window.print_window()
            window.action = False
        time.sleep(1)
        os.system("clear")
        window.clear_window()
        drone.move('left')



