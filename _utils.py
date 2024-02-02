import bcolors
from room import Room
from player import Player
from game import Game
from bcolors import colors

def printc(msg, color_in):
    """Pretty printing with colors"""

    colors = bcolors.colors
    print(f"{colors[color_in]}", f"{msg}", colors["g"])
    # This section is for showing example text & it's key
    if msg == "x":
        for ex_color in colors:
            print(f"{colors[ex_color]}", "EXAMPLE", "| ", ex_color, colors["g"])
