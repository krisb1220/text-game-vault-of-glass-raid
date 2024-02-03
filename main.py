import bcolors
from room import Room
from player import Player
from game import Game
from _utils import printc
import storylines

#New Code

my_room = ''

my_room = Room("Start", "NONE")
rooms = [my_room]
player = Player("Kris")
game = Game(player, rooms)
state = game.get_state()

player_inputs = [

]


def reject_command():
    game.commands.pop(0)
    game.command_current = "ERROR"
    game.commands.insert(0, game.command_current)
    printc("oops, may want to try that again", "f")

def next(step):
    step1=state["current_step"]
    print("step begin", step1)
    game.set_state(["current_step", step+1])
    game.set_state(["move_on", True])
    print("step end", step1)
    print("step after", step1)



def process_inputs(i, in_type):
    print("input user")
    if in_type == "lines":
        print(storylines.lines[i])

    # if type == "choices":
    #     for choice in storylines.lines[0]:
    #         i = i + inc
    #         print(choice)

def start(step):
    game.start()
    process_inputs(0, "lines")
    player.name = input("What is your name?")

def updateRoom(newRoom):
    game.set_state(["current_room", newRoom])

def run_command(runner):

    """
    A function that dispatches correct commands to their respective functions
    and outcomes.
    """

    game.commands.insert(0, runner) # log the command into the command array

    if runner == "end":
        game.end(False)

# internal commands

    elif runner == "start":
        start(0)

    elif runner == "_change_room":
        printc("x", "a")

    else:
        reject_command()



while game.state["is_running"]:
    game.command_current = input("Enter a command:")
    cmds = game.commands

    print(game.state["move_on"])



    if state["win_condition"]:
        game.end(True)

    if not state["is_running"]:
        run_command("start")

    if state["move_on"] and state["current_step"] != len(storylines.lines):
        print("lines", len(storylines.lines))
        process_inputs(state["current_step"], "lines")
        state["move_on"] = False
        next(state["current_step"])


    if cmds[0] in game.valid_commands:
        run_command(game.command_current)







