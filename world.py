from random import randint, shuffle
from config import *
from time import sleep
from os import system

ENTRY = randint(int(HEIGHT * 0.25), int(HEIGHT * 0.75))

class World:

    def __init__(self, worms):
        self.grid = self.create_scenery()
        for w in worms:  # is this weird?
            w.grid = self.grid
        shuffle(worms)
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



    def display_scenery(self, current_turn=None):
        if current_turn is not None:
            worm_whose_turn = list(" ↙ " + (current_turn.name.split(" ")[0]))
            print(current_turn.x, current_turn.y)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                if current_turn and current_turn.name_pos_check(x, y) and len(worm_whose_turn):
                    print(worm_whose_turn.pop(0), end="")
                else:
                    for w in self.worms:
                        if w.x == x and w.y == y:
                            print(w.symbol, end="")
                            break
                    else:
                        print(cell, end="")
            print()

