

from game import Game


# bomb!

# 1 message queue fixes X
# 2 fix index error start bug + randomise slightly starting y indices X
# 3 implement jump w/ custom height X
# 4 implement jump followed by fall X
# 5 fix maximum Y bound bug - dead if on platform
# 6 prevent jumping off side of screen X
# 7 stack up land X
# 8 worms are always falling ish
# 9 implement 'gun' animation
# refactor sprite class
# 10 implement 'mine' animation
# 11 implement 'bomb' animation
# 12 implement worm damage  / HP
# 13 implement terrain damage
#


if __name__ == "__main__":

    game = Game()
    game.main_game_loop()