from config import *

class Sprite:

    def __init__(self, x, y, symbol, visible):

        self.x = x
        self.y = y
        self.symbol = symbol
        self.visible = True

    def set_grid(self, grid):
        self.grid = grid


    def check_out_of_bounds(self, check_horiz=True, check_bottom=False, check_top=False, out_of_bounds_next_step=print):
        reset_y, reset_x = None, None


        if check_bottom and self.y > HEIGHT-1:
            reset_y = HEIGHT-1
        if check_top and self.y < 0:
            reset_y = 0

        if check_horiz:
            if self.x > WIDTH - 1:
                reset_x = WIDTH - 1
            elif self.x < 0:
                reset_x = 0

        if reset_y is not None:
            self.y = reset_y

        elif reset_x is not None:
            self.x = reset_x

        else:
            return False

        out_of_bounds_next_step() # call bound function to deal with out-of-bounds
        return True


