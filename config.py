import platform

if platform.system() ==  "Windows":
    CLEAR = "CLS"
else:
    CLEAR = "clear"

WORMS_PER_TEAM = 5
HEIGHT = 30
WIDTH = 200
FRAME_SPEED = 0.25
TEAM_WAIT_TIME = 2
NAME_DISTANCE = 1
MIN_GAP_LENGTH = 2
MAX_GAP_LENGTH = 7