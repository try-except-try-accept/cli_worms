
from config import *
from helpers import get_death_msg, get_gravestone, get_boundary_msg
from random import randint, choice as rand_choice
from sprite import Sprite

class Worm(Sprite):
    def __init__(self, name, team, start_x, symbol, msg_queue):
        x = start_x
        y = randint(-WORMS_PER_TEAM, 0)
        super().__init__(x, y, symbol, False, name)

        self.msgs = msg_queue

        self.team = team
        self.dead = False
        self.jump_queue = []
        self.jumping = False
        self.frame_speed = FRAME_SPEED
        self.fall_momentum = FRAME_SPEED
        self.gender = rand_choice(["male", "female"])

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        '''Allow leftmost worm to be selected for testing'''
        return self.x < other.x

    def out_of_bounds_msg(self):
        self.msgs.append(get_boundary_msg(self.name, self.gender))

    def die(self):
        self.symbol = get_gravestone()
        self.label = ""
        self.dead = True
        self.msgs.append("{} {} {}".format(self.symbol, self.name, get_death_msg(0, self.gender)))

    def fall(self):
        '''Increase y axis to fall, return True if make contact
        with scenery - False if not yet'''


        if self.dead:   return True, 1

        if self.grid[self.y][self.x] == " ":
            self.y += 1
            self.fall_momentum *= GRAVITY

            if self.y >= 0:          # random fall points - do not show until visible
                self.visible = True

            if self.check_out_of_bounds(check_bottom=True, check_horiz=False, out_of_bounds_next_step=self.die):
                return True, self.fall_momentum


            return False, self.fall_momentum

        self.fall_momentum = FRAME_SPEED
        return True, self.fall_momentum

    def interrupt_if_dead(func):    # is this an appropriate use of a decorator?
        def inner(self, direction, frame):

            if self.dead:
                return 0, STOP_ANIMATION
            else:
                return func(self, direction, frame)

        return inner

    def end_action(self):
        self.jumping = False


    @interrupt_if_dead
    def jump(self, direction, frame_countdown):

        x_vel = 1 if direction == "r" else -1
        falling = False

        if not self.jumping: # start of jump so populate queue
            self.jumping = True
            self.jump_queue = ([1] * frame_countdown) + ([-1] * frame_countdown)
            self.frame_speed = FRAME_SPEED / 1.75
            self.y -= 1

        elif self.check_out_of_bounds(): # hit edge of screen so start to fall
            falling = True
        else:
            if self.grid[self.y][self.x] != " ":  # jump complete - hit platform
                return self.frame_speed, STOP_ANIMATION
            elif len(self.jump_queue):     # yet to complete jump
                y_vel = self.jump_queue.pop(0)
                if y_vel > 0:
                    self.frame_speed /= GRAVITY
                else:
                    self.frame_speed *= GRAVITY
                self.x += x_vel
                self.y -= y_vel
            else:                       # finished jump, no platform, must be falling!
                falling = True

        if falling:
            landed, momentum = self.fall()
            if landed:
                return momentum, STOP_ANIMATION

        return self.frame_speed, frame_countdown

    @interrupt_if_dead
    def move(self, direction, frame_countdown):
        vel = 1 if direction == "r" else -1

        landed, momentum = self.fall()  # if falling, cannot move until grounded.
        if not landed:
            return momentum, 1 if frame_countdown < 1 else frame_countdown




        self.frame_speed += 0.01

        if vel == -1 and self.grid[self.y][self.x] == "\\":
             self.y -= 1
        elif vel == 1 and self.grid[self.y][self.x] == "/":
             self.y -= 1


        if self.check_out_of_bounds(out_of_bounds_next_step=self.out_of_bounds_msg):
            return self.frame_speed, STOP_ANIMATION

        self.x += vel

        return self.frame_speed, frame_countdown - 1


