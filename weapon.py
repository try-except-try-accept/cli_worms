from config import *
from sprite import Sprite

class Weapon(Sprite):

    def __init__(self, x, y, grid):

        super().__init__(x, y, '', False)
        super().set_grid(grid)
        self.explosion_queue = list(EXPLOSIONS)





class Arrow(Weapon):

    def __init__(self, x, y, grid, parent_list):
        super().__init__(x, y, grid)
        self.parent_list = parent_list


    def delete(self):
        self.parent_list.remove(self)


    def fire(self, cmd, direction):
        self.x += D_MAP[direction][0]
        self.y += D_MAP[direction][1]
        self.symbol = D_MAP[direction][2]

        if self.check_out_of_bounds(check_vert=True, resultant_action=self.delete):
            return 0, 0


        if self.grid[self.y][self.x] != " ":
            if len(self.explosion_queue):
                self.symbol = self.explosion_queue.pop(0)
            else:
                self.visible = False
                return 0.125, 0



        return 0.125, direction

