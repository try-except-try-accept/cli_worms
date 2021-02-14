from random import randint
from config import *
from time import sleep
from os import system

ENTRY = randint(int(HEIGHT * 0.25), int(HEIGHT * 0.75))

class World:

    def __init__(self, worms):
        self.grid = self.create_scenery()
        for w in worms:  # is this weird?
            w.grid = self.grid
        self.worms = worms





    def air_drop(self):
        grounded = [False] * (WORMS_PER_TEAM * 2)
        while not all(grounded):
            grounded = [w.fall() for w in self.worms]
            self.display_scenery()
            sleep(FRAME_SPEED)
            system("clear")








    def create_scenery(self):
        grid = [[' ' for i in range(WIDTH)] for j in range(HEIGHT)]

        y = ENTRY

        draw = True
        try:
            for x in range(WIDTH):

                if draw:
                    if not randint(0, 1):
                        # go straight
                        grid[y][x] = "_"
                    elif not randint(0, 1):
                        # drop down
                        y += 1
                        grid[y][x] = "\\"
                    else:
                        # go up
                        grid[y][x] = "/"
                        y -= 1

        except:
            pass

        return grid

    def display_scenery(self):
        worm_pos = {[w.y, w.x] for w in self.worms}

        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if [y, x] in worm_pos:
                    print("S", end="")
                else:
                    print(col, end="")
            print()

