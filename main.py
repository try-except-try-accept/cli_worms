

from game import Game


# bomb!

# 1 message queue fixes X
# 2 fix index error start bug + randomise slightly starting y indices X
# 3 implement jump w/ custom height X
# 4 implement jump followed by fall X
# 5 fix maximum Y bound bug - dead if on platform
# 6 prevent jumping off side of screen X
# 7 stack up land X
# 8 worms are always falling ish - gravity refactor X
# 8b stop being able to jump through terrain X
# 9 implement 'gun' animation X
# 9b shoot angle X
# refactor sprite class X
# garbage collect X
# 10 implement 'mine' animation X
# 10a frame handler - all worms and mines run func per frame
# 10b worms fall through gaps caused by mines
# 11 implement 'grenade' animation - parabola, explode on impact
# 12 implement worm damage  / HP
# 13 implement terrain damage for arrows
# 14 weapon select
#


if __name__ == "__main__":

    game = Game()
    game.main_game_loop()