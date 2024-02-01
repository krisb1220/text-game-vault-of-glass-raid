import bcolors
from room import Room
from player import Player
from game import Game
from bcolors import colors
from _utils import printc

room_instance = Room("Living Room")
player = Player("Kris")
game = Game(Player)

class _globals:

    def __init__(self):
        self.command_current = "start"
        self.command_count = 0
        self.commands = ['start']
        self.valid_commands = [
            "test",
            "colors",
            "end",
            "start",
            "ERROR"
    ]


my_game = _globals()

print(my_game.command_count)

game.start()


def reject_command(cmd):
    my_game.commands.pop(0)
    my_game.command_current = "ERROR"
    my_game.commands.insert(0, my_game.command_current)
    printc("command not recognized", "a")
    print(my_game.commands)

def send_command(cb):
    print("command sent")

    if cmd[0] == "test":
        printc("everything is good", "g")
        print(my_game.commands)

        # send_command(cmd_inc(1))

    elif cmd[0] == "end":
        game.end(False)

    elif cmd[0] == "colors":
        printc("x", "a")

    elif cmd[0] == "Begin":
        printc("x", "a")

    else:
        reject_command(cmd)
        printc("command not recognized", "f")
        # cmd.insert(0, input("Enter a command:"))

    return cb

while game.state["isRunning"]:
    cmd = my_game.commands #commands array
    # my_game.command_current = input("Enter a command:")

    if cmd[0] in my_game.valid_commands:
        cmd.insert(0, my_game.command_current)
        send_command("test")

    if cmd[0] not in my_game.valid_commands:
        reject_command(cmd)





