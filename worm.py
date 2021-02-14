
from config import *
from helpers import get_death_msg, get_gravestone

class Worm:
    def __init__(self, name, team, start_x, symbol, message_queue):
        self.msgs = message_queue
        self.name = name
        self.team = team
        self.symbol = symbol
        self.x = start_x
        self.y = 0
        self.dead = False

    def fall(self):
        '''Increase y axis to fall, return True if make contact
        with scenery - False if not yet'''
        if self.dead:   return True

        if self.grid[self.y][self.x] == " ":
            self.y += 1
            if self.y == len(self.grid) - 2:
                self.symbol = get_gravestone()
                self.dead = True
                self.msgs.append("{} {}".format(self.name, get_death_msg(0)))
                return True
            return False
        else:
            return True


    def move(self, direction, value):
        if self.dead:
            return 0

        d = 1 if direction == "right" else -1

        if self.grid[self.y+1][self.x] in ["/", "\\"]:
            self.y += 1
        elif self.grid[self.y][self.x] in ["/", "\\"]:
            self.y -= 1
        elif self.grid[self.y][self.x] == "_":
            pass
        else:
            if self.fall():
                return 0
            else:
                return value + 1
        self.x += d
        return value







    def name_pos_check(self, grid_x, grid_y):
        '''Check grid pos against worm pos, return True if name
        of worm should be displayed'''
        if grid_x >= self.x:
            if grid_y == self.y - NAME_DISTANCE:
                return True
        return False

