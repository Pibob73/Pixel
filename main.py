#!/usr/bin/env python3
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
from Player import Player
from math import sin, cos, pi
import sys
import select
import asyncio
import map
import random
def get_char():
    letter = ''
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        letter =sys.stdin.read(1)
    return letter

if __name__ == "__main__":
    heightWindow = 23
    widthWindow = 80
    window = Window(23, 120)
    exitProgramme = False
    drone = []
    drone.append(Drone([8, 20], '@', window))
    drone[0].create_drone()
    player = Player()
    unit = Drone([9, 9], '@', window, color='\033[32m')
    unit.create_drone()
    dog = Drone([10, 39], 'd', window, direction='left')
    directions_drone = ['left','down','right','up']
    directions_dog = ['right','left']
    corner = 1
    task_dog = 0
    task_drone = 0
    while not exitProgramme:
        map.castle(window)
        #Block([6, 4], [10, 10], '*', window, color='\033[36m', floor=True).create_block()
        if window.action or True:
            time.sleep(0.1)
            os.system("clear")
            Fill([1, 1], ',', window, color='\033[32m').fill()
            window.print_window()
            window.action = False
        window.clear_window()
        if drone:
            drone[0].direction = directions_drone[random.randrange(4)]
            drone[0].move(drone[0].direction)
            #print(drone[0].position[0], drone[0].position[1], sep=',')
            if drone[0].danger_zone():
                drone.pop(0)
        X = int(50 + 3 * cos(corner))
        Y = int(10 + 2 * sin(corner))
        corner += 1
        dog.position = [Y, X]
        dog.move()
        if corner == 45:
            corner = 0
        Text('inventory: {}'.format(player.bag[0]), [15, 83], window, color='\033[37m').print_text()
        Text('heart: ♥ ♥ ♥ ♥ ♥ ', [19, 83], window, color='\033[31m').print_text()
        player.move_player(get_char())
        unit.move(player.direction)
        #player.direction = ''

        #dog.move(dog.direction)


