import IPython #import2
from room import Room
room_instance = Room("Living Rom")


print(room_instance.room)  # Accessing the property
room_instance.room = "Bedroom"  # Setting the property
print(room_instance.room)  # Accessing the property again

print(room_instance)


