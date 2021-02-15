from config import *

class Sprite:

    def __init__(self, x, y, symbol, visible):

        self.x = x
        self.y = y
        self.symbol = symbol
        self.visible = True

    def set_grid(self, grid):
        self.grid = grid


    def check_out_of_bounds(self, check_horiz=True, check_vert=False, resolve_position=True, resultant_action=print):
        if not check_horiz:
            if self.y > HEIGHT-1:
                if resolve_position:
                    self.y = HEIGHT-2
                return True
            elif self.y < 0:
                if resolve_position:
                    self.y = 0
                return True
        else:
            if self.x > WIDTH - 1:
                if resolve_position:
                    self.x = WIDTH - 1
                return True
            elif self.x < 0:
                if resolve_position:
                    self.x = 0
                return True
        return False