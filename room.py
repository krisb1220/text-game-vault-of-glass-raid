class Room:
    """A class representing a generic room"""

    def __init__(self, room_name, item):
        self.room_name = room_name
        self.is_occupied = False
        self.item = ''
        self.portals = []
        self.minigame = []

    @property
    def room(self):
        """Get the room name"""
        return self.room_name

    @room.setter
    def room(self, new):
        """Change the room name"""
        self.room_name = new

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"

    def get(self):
        return self