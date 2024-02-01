class Player:
    """A class representing a generic room"""

    def __init__(self, name):
        self._name = name
        self._position = []
        self._inventory = []
        self._count = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new):
        self._position.insert(0, new)

    def update_position(self, new):
        self._position.insert(0, new)
        return self._position

    def go_backwards(self):

        if self.position:
            self._position.pop(0)
        else:
            return "No options"

        return self.position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new


    def __str__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        formatted_attributes = ',\n'.join(f"{attr} = {attributes[attr]}" for attr in attributes)
        return f"{class_name} {{\n{formatted_attributes}\n}}"
