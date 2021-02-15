

from game import Game


# bomb!

# 1 message queue fixes
# 2 fix index error start bug + randomise slightly starting y indices
# 3 implement jump w/ custom height
# 4 implement jump followed by fall
# 5 fix maximum Y bound bug - dead if on platform
# 6 prevent jumping off side of screen
# 7 implement bomb
# 8 implement 'gun'
#
#
#


if __name__ == "__main__":

    game = Game()
    game.main_game_loop()