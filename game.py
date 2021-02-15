from time import sleep
from json import loads

from helpers import random_name, get_losing_team_msg
from world import World

from worm import Worm

from os import system
from random import randint

from config import *

class Game:

    def __init__(self):
        self.msg_queue = []
        self.msg_history = []

        self.welcome()
        self.teams = {}
        worms = self.create_worms()
        self.world = World(worms, self.msg_queue, self.msg_history)
        self.game_over = False

    def check_end_game(self):
        for team, worms in self.teams.items():
            if all([w.dead for w in worms]):
                self.msg_queue.append("{} {}".format(team, get_losing_team_msg()))
                return True
        return False

    def welcome(self):
        print(LOGO)

    def create_worms(self):
        gen = False
        if not input(CONFIG_MSGS["input_or_generate"]):
            gen = True

        worms = []
        p = 0
        for team_symbol in ["S", "Ƨ"]:
            p += 1
            if gen:
                team = random_name()
            else:
                print(f"Player {p} ({team_symbol}) --- enter team name:\n\n")
                team = input()
                while len(team) < 4:
                    team = input("No - please give a team name: ")

            print("""
            
Player {} --- your team will be named:
            
{}
""".format(p, team.upper()))
            self.teams[team] = []
            sleep(INTRO_FRAME_SPEED)

            for i in range(1, WORMS_PER_TEAM + 1):
                if gen:
                    worm_name = random_name(True)
                else:
                    print(f"Player {p} --- enter name for worm {i}:\n\n")
                    worm_name = input()
                    while len(worm_name) < 4:
                        worm_name = input("No - please give a worm name: ")

                print("{0} joined {1}!!!".format(worm_name.upper(), team))
                sleep(randint(MIN_TEAM_SIGNUP, MAX_TEAM_SIGNUP))

                x_pos_used = []

                start_x = randint(1, WIDTH-2)

                while start_x in x_pos_used:
                    start_x = randint(1, WIDTH-2)
                new_worm = Worm(worm_name, team, start_x, team_symbol, self.msg_queue)
                worms.append(new_worm)
                self.teams[team].append(new_worm)
                x_pos_used.append(start_x)

        return worms

    def action_help(self):
        print("")
        for a, min_, max_, exp in ACTIONS:
            print(f"   - Type {a} x to {exp}. Minimum value for x is {min_}, maximum is {max_}.")
        print()

    def validate_action(self, command):
        if command == "help":
            return self.action_help()
        try:
            cmd, param = command.split(" ")
        except:
            return False
        for a, min_, max_, exp in ACTIONS:
            if cmd == a:
                if param.isdigit():
                    param = int(param)
                    if param >= min_ and param <= max_:
                        return True
        return False

    def display_game_and_cli(self, special_data=None):
        worm = special_data if type(special_data) == Worm else None
        system(CLEAR)
        self.world.display_scenery(worm)
        self.world.display_msg_history()
        self.world.display_msg_queue()

    def main_game_loop(self):

        self.world.air_drop()

        game_over = False
        while not game_over:

            for worm in self.world.worms:

                if TEST_MODE:
                    worm = min([w for w in self.world.worms if not w.dead])

                game_over = self.check_end_game()

                if game_over:
                    break

                if not worm.dead:
                    self.display_game_and_cli(worm)

                    print()
                    sleep(1)

                    turn_msg = f"It's {worm.name}'s turn ({worm.team})"
                    self.msg_history.append(turn_msg.replace("It's", "It was"))
                    print(turn_msg)
                    action = input("Enter a command or type HELP for guidance! ")
                    while not self.validate_action(action):
                        action = input("Enter a command: ")
                    self.msg_history.append(f"{worm.name} decided to *{action}*")

                    self.world.enact(worm, action)

            self.display_game_and_cli()