
from config import *
from helpers import get_death_msg

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
        try:
            if self.grid[self.y][self.x] == " ":
                self.y += 1
                return False
            else:
                return True
        except IndexError:
            self.dead = True
            self.msgs.append("{} {}".format(self.name, get_death_msg(0)))

    def name_pos_check(self, grid_x, grid_y):
        '''Check grid pos against worm pos, return True if name
        of worm should be displayed'''
        if grid_x >= self.x:
            if grid_y == self.y - NAME_DISTANCE:
                return True
        return False

