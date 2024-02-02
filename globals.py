class Globals:
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