class Room:
    """A class representing a generic room"""

    def __init__(self, room_name):
        self.room_name = room_name
        self.is_occupied = False
        self.item = ''
        self.portals = []

    @property
    def room(self):
        """Get the room name"""
        return self.room_name

    @room.setter
    def room(self, new):
        """Change the room name"""
        self.room_name = new
