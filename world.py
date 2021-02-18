from random import randint, shuffle
from config import *
from time import sleep
from os import system
from helpers import get_airdrop_msg
from weapon import Arrow

ENTRY = randint(int(HEIGHT * 0.33), int(HEIGHT * 0.66))

class World:

    def __init__(self, worms, msg_queue, msg_history):
        self.grid = self.create_scenery()
        self.msg_queue = msg_queue # is this weird? am i allowed to pass a list between objects
        self.msg_history = msg_history
        # so everything 'knows about' it ?
        for w in worms:  # is this weird?
            w.set_grid(self.grid)
        shuffle(worms)
        self.worms = worms
        self.uxo = []

    def display_msg_history(self):
        print()
        print()
        print("\n".join(self.msg_history[-5:]))

    def display_msg_queue(self):
        while len(self.msg_queue) > 0:
            msg = self.msg_queue.pop(0)
            self.msg_history.append(msg)
            print(msg)
            sleep(MESSAGE_QUEUE_FRAME_RATE)


    def weapons_test(self):

        ox, oy = WIDTH // 2, HEIGHT // 2
        max_x, max_y = ox+10, oy+10
        min_x, min_y = ox-10, oy-10
        for i, j in ANGLES:
            x, y = ox, oy
            symbol = chr(randint(65, 90))

            while x < WIDTH and min_x< x<max_x and y < HEIGHT and min_y<y<max_y:
                self.grid[y][x] = symbol
                x += i
                y += j
                print()
                self.display_scenery()

                sleep(0.1)
                system(CLEAR)
            self.display_scenery()

            self.display_msg_history()
            m = "{}: tested {} {}".format(symbol, i, j)
            print(m)
            self.msg_history.append(m)
            input()


    def air_drop(self, start_game=True, dropped_items=None):

        if not start_game:
            msg = get_airdrop_msg()
            print(msg)
            sleep(1)
            self.msg_history.append("msg")
            self.msg_history.append("An airdrop was received.")
            countdown = 3

        else:
            countdown = 10
            dropped_items = self.worms

        print("Commencing airdrop in...")
        sleep(INTRO_FRAME_SPEED)
        for i in range(countdown, -1, -1):
            print(f" {i}")
            sleep(INTRO_FRAME_SPEED / 4)
        print("AWAY!")
        sleep(INTRO_FRAME_SPEED * 2)
        system(CLEAR)

        grounded = [False] * (WORMS_PER_TEAM * 2)
        while not all(grounded):
            system(CLEAR)
            falling_data = [w.fall() for w in dropped_items]
            frame_speed = sum([w[1] for w in falling_data]) / len(falling_data)
            grounded = [w[0] for w in falling_data]
            self.display_scenery()
            self.display_msg_history()
            sleep(frame_speed)

        system(CLEAR)

    def remove_weapon(self, item):
        self.uxo.remove(item)

    def convert_action(self, action_frame):
        try:
            return int(action_frame)
        except ValueError:
            return ORIENTATIONS.index(action_frame)

    def enact(self, worm, action):
        command, action_frame = action.lower().split(" ")
        action_frame = self.convert_action(action_frame)

        if command in ["left", "right"]:
            func = worm.move
        elif command in ["ljump", "rjump"]:
            func = worm.jump
        elif command in ["shoot"]:
            projectile = Arrow(worm.x, worm.y, self.grid, self.remove_weapon)
            self.uxo.append(projectile)
            func = self.uxo[-1].fire

        while action_frame >= 0:
            system(CLEAR)
            frame_speed, action_frame = func(command[0], action_frame)

            self.display_scenery()
            self.display_msg_history()
            sleep(frame_speed)

        worm.end_action()

    def create_scenery(self):
        grid = [[' ' for i in range(WIDTH)] for j in range(HEIGHT)]

        y = ENTRY

        draw = 0   # miss out platform chunks if > 0.
        try:
            for x in range(WIDTH):

                if not draw:
                    if randint(0, 1):
                        # go straight
                        grid[y][x] = "_"
                        grid[y+1][x] = "_"
                        grid[y+2][x] = "_"
                    elif randint(0, 1):
                        # drop down
                        y += 1
                        grid[y][x] = "\\"
                        grid[y+1][x] = "\\"
                        grid[y+2][x] = "\\"
                    else:
                        # go up
                        grid[y][x] = "/"
                        grid[y+1][x] = "/"
                        grid[y+2][x] = "/"
                        y -= 1

                if not randint(0, 6):
                    draw = randint(MIN_GAP_LENGTH, MAX_GAP_LENGTH)

                if draw > 0:
                    draw -= 1

        except:
            pass

        return grid

    def display_scenery(self, current_turn=None):
        if current_turn is not None:
            worm_whose_turn = list(" ↙ " + (current_turn.name.split(" ")[0]))

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                if current_turn and current_turn.name_pos_check(x, y) and len(worm_whose_turn):
                    print(worm_whose_turn.pop(0), end="")
                else:
                    for sprite in self.worms + self.uxo:
                        if sprite.visible and sprite.x == x and sprite.y == y:
                            print(sprite.symbol, end="")
                            break

                    else:
                        print(cell, end="")
            print()



