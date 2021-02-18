from config import *
from sprite import Sprite

class Weapon(Sprite):

    def __init__(self, x, y, grid, destructor ):

        super().__init__(x, y, '', False)
        super().set_grid(grid)
        self.explosion_queue = list(EXPLOSIONS)
        self.destructor = destructor
        self.existence = 0


    def delete(self):
        self.destructor(self)





class Arrow(Weapon):

    def __init__(self, x, y, grid, destructor):
        super().__init__(x, y, grid, destructor)



    def fire(self, cmd, direction):
        self.existence += 1

        octile = (direction // 45)

        x_vel = D_MAP[octile][0]
        y_vel = D_MAP[octile][1]

        self.symbol = D_MAP[octile][2]

        octile_offset = direction % 45

        if octile_offset != 0:
            axis_alter = octile_offset//3
            if direction % 2 == 0:
                x_vel *= axis_alter
                y_vel *= (axis_alter - 1)

            else:
                y_vel *= axis_alter
                x_vel *= (axis_alter - 1)



        self.x += x_vel
        self.y += y_vel

        frame_rate = FRAME_SPEED * max([1, x_vel, y_vel])

        if self.check_out_of_bounds(check_top=True, check_bottom=True, check_horiz=True, out_of_bounds_next_step=self.delete):
            return 0, STOP_ANIMATION


        if self.grid[self.y][self.x] != " " or self.existence > ARROW_LIFE:
            if len(self.explosion_queue):
                self.symbol = self.explosion_queue.pop(0)
            else:
                self.visible = False
                return frame_rate, -1



        return frame_rate, direction

