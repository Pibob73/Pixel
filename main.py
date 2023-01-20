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
import map
import random


if __name__ == "__main__":
    heightWindow = 23
    widthWindow = 80
    window = Window()
    exitProgramme = False
    drone = Drone([8, 20], '@', window)
    drone.create_drone()
    dog = Drone([10, 6], 'd', window, direction='right')
    directions_drone = ['left','down','right','up']
    directions_dog = ['right','left']
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
        drone.direction = directions_drone[random.randrange(4)]
        print(drone.position[0], drone.position[1], sep=',')
        if dog.can_move(directions_drone[task_dog]):
            task_dog += 1
            if task_dog >= len(directions_drone):
                task_dog = 0
            dog.direction = directions_drone[task_dog]
        drone.move(drone.direction)
        dog.move(dog.direction)


