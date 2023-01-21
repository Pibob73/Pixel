import os
import time
from Line import Line
from Window import Window
from Box import Box
from Letter import Letter
from Text import Text
from Circle import Circle
from Pixel import Pixel
from Fill import Fill
from Drone import Drone
from Ring import Ring
from Block import Block
from Empty import Empty
def test_map(window):
    Box([0, 0], [22, 79], '#', window, color='\033[35m').create_block()
    Box([5, 5], [17, 74], '█', window, color='\033[36m').create_block()
    Box([2, 3], [16, 73], '█', window, head=True, floor=True, color='\033[36m').create_block()
    Circle([11, 40], 10, '$', window).create_circle()
    Line('▂', [10, 20], 30, 'right', window, head=True, color='\033[32m').create_line()
    Line('*', [6, 3], 17, 'right', window, head=True).create_line()
    Text('I LOVE YOU', [2, 30], window, head=True).print_text()
    Text('CAR ||', [5, 30], window, head=True, color='\033[31m').print_text()
    Circle([5, 5], 10, '%', window).create_circle()
    Circle([13, 8], 5, '%', window, color='\033[32m', head=True).create_circle()
    window.create_position(Letter('0', color='\033[33m', head=True), 13, 8)
    window.create_position(Letter('a', color='\033[31m', head=True), 14, 10)
    window.create_position(Letter('a', color='\033[31m', head=True), 12, 7)
    Pixel('=', [8, 60], 6, window, color='\033[31m', floor=True).create_pixel()
    window.create_position(Letter('*', color='\033[33m', head=True), 2, 29)
    window.create_position(Letter('*', color='\033[33m', head=True), 2, 40)
    window.create_position(Letter('♚', color='\033[37m'), 9, 8)
    Ring([5, 70], 20, '█', window).create_circle()
    Circle([5, 70], 14, '+', window).create_circle()

def car(row, column, window):
    window.create_position(Letter('0', color='\033[30m'), row - 1,
                                column + 2)
    window.create_position(Letter('0', color='\033[30m'), row - 1,
                                column - 2)
    window.create_position(Letter('0', color='\033[30m'), row + 1,
                                column + 2)
    window.create_position(Letter('0', color='\033[30m'), row + 1,
                                column - 2)
    Circle([row, column], 2, '#', window, color='\033[31m').create_circle()


def tower(row, column, window):
    Ring([row, column], 20, '█', window, color='\033[37m', let=True).create_circle()
    Circle([row, column], 19, '+', window).create_circle()
def castle(window):
    window.create_position(Letter('+', color='\033[033m'), 9, 9)
    window.create_position(Letter('+', color='\033[033m'), 5, 16)
    tower(5, 9, window)
    window.create_position(Letter('+', color='\033[033m'), 5, 62)
    window.create_position(Letter('+', color='\033[033m'), 9, 69)
    tower(5, 69, window)
    window.create_position(Letter('+', color='\033[033m'), 12, 9)
    window.create_position(Letter('+', color='\033[033m'), 16, 16)
    tower(16, 9, window)
    window.create_position(Letter('+', color='\033[033m'), 12, 69)
    window.create_position(Letter('+', color='\033[033m'), 16, 62)
    tower(16, 69, window)
    Block([18, 0], [23, 80], '~', window, color='\033[36m', floor=True).create_block()
    Block([0, 0], [4, 80], '~', window, color='\033[36m', floor=True).create_block()
    Block([0, 0], [23, 4], '~', window, color='\033[36m', floor=True).create_block()
    Block([0, 75], [23, 80], '~', window, color='\033[36m', floor=True).create_block()
    Block([4, 33], [17, 36], '~', window, color='\033[31m', floor=True, danger=True).create_block()
    Block([4, 16], [5, 62], '█', window, head=True, color='\033[37m', let=True).create_block()
    Block([8, 4], [13, 6], '█', window, head=True, color='\033[37m', let=True).create_block()
    Block([4, 16], [5, 62], '█', window, head=True, color='\033[37m', let=True).create_block()
    Block([17, 16], [18, 62], '█', window, head=True, color='\033[37m', let=True).create_block()
    Block([8, 73], [14, 75], '█', window, head=True, color='\033[37m', let=True).create_block()
    Box([0, 80], [22, 119], '█', window, color='\033[35m').create_block()
    Text('SEA CASTLE', [2, 33], window, color='\033[36m', head=True).print_text()
