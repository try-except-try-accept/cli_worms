
from config import *

class Worm:
    def __init__(self, name, team, start_x, symbol):
        self.name = name
        self.team = team
        self.symbol = symbol
        self.x = start_x
        self.y = 0

    def fall(self):
        '''Increase y axis to fall, return True if make contact
        with scenery - False if not yet'''
        if self.grid[self.y][self.x] == " ":
            self.y += 1
            return False
        else:
            True