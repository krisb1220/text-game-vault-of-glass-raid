class Game:
    """A class representing a generic room"""

    def __init__(self, player):

        self.state = {
            "isRunning": False,
            "win_condition": False
        }
        self.player = player #dict

    def set_state(self, new):
        self.state[new[0]] = new[1]

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

