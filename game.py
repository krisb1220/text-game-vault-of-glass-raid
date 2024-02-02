class Game:
    """A class representing a generic room"""

    def __init__(self, player, rooms):

        self.state = {
            "is_running": True,
            "win_condition": False,
            "currentRoom": 0,
            "current_step": 0,
            "move_on": True
        }

        self._rooms = rooms
        self.player = player
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

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, new):
        self._rooms = new

    def set_state(self, new):
        self.state[new[0]] = new[1]

    def get_state(self):
        return self.state

    def start(self):
        self.state["isRunning"] = True

    def end(self, result):
        self.state["win_condition"] = result
        self.state["isRunning"] = False

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"

