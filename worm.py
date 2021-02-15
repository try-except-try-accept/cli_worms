
from config import *
from helpers import get_death_msg, get_gravestone, get_boundary_msg
from random import randint

class Worm:
    def __init__(self, name, team, start_x, symbol, msg_queue):
        self.msgs = msg_queue
        self.name = name
        self.team = team
        self.symbol = symbol
        self.x = start_x
        self.y = randint(-WORMS_PER_TEAM, 0)
        self.dead = False
        self.visible = False
        self.jump_queue = []
        self.jumping = False
        self.frame_speed = FRAME_SPEED

    def fall(self):
        '''Increase y axis to fall, return True if make contact
        with scenery - False if not yet'''
        if self.dead:   return True

        if self.grid[self.y][self.x] == " ":
            self.y += 1

            if self.y >= 0:          # random fall points - do not show until visible
                self.visible = True

            if self.y == len(self.grid) - 2:
                self.symbol = get_gravestone()
                self.dead = True
                self.msgs.append("{} {} {}".format(self.symbol, self.name, get_death_msg(0)))
                return True
            return False
        else:
            return True

    def interrupt_if_dead(func):    # is this an appropriate use of a decorator?
        def inner(self, direction, frame):

            if self.dead:
                return 0
            else:
                return func(self, direction, frame)

        return inner

    @interrupt_if_dead
    def jump(self, direction, frame):
        x_vel = 1 if direction == "r" else -1


        if not self.jumping: # start of jump so populate queue
            self.jumping = True
            self.jump_queue = ([1] * frame) + ([-1] * frame)
            self.frame_speed = FRAME_SPEED / 1.5
            return self.frame_speed, frame
        else:

            try:
                y_vel = self.jump_queue.pop(0)

                self.frame_speed += y_vel/300
                #print("Frame speed is {}".format(self.frame_speed))

                self.x += x_vel
                self.y -= y_vel

                if self.grid[self.y][self.x] != " ":  # jump complete - platform
                    return self.frame_speed, 0

                return self.frame_speed, frame

            except IndexError:
                if self.grid[self.y][self.x] == " ": # jump complete - but now falling!
                    landed = self.fall()
                    if not landed:
                        return self.frame_speed, frame
                    else:
                        return self.frame_speed, 0
                else:
                    self.jumping = False
                    return self.frame_speed, 0 # jump complete - platform!





    @interrupt_if_dead
    def move(self, direction, frame):
        # if self.dead:
        #     return 0

        vel = 1 if direction == "r" else -1

        self.frame_speed += 0.01

        if self.grid[self.y+1][self.x] in ["/", "\\"]:
            self.y += 1
        elif self.grid[self.y][self.x] in ["/", "\\"]:
            self.y -= 1
        elif self.grid[self.y][self.x] == "_":
            pass
        else:
            if self.fall():
                return self.frame_speed, 0
            else:
                return self.frame_speed, frame

        if self.x == 0 or self.x == WIDTH-1:
            self.msgs.append(get_boundary_msg(self.name))
            return self.frame_speed, 0
        self.x += vel
        return self.frame_speed, frame - 1







    def name_pos_check(self, grid_x, grid_y):
        '''Check grid pos against worm pos, return True if name
        of worm should be displayed'''
        if grid_x >= self.x:
            if grid_y == self.y - NAME_DISTANCE:
                return True
        return False

