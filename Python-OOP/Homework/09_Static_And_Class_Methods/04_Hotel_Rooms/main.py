from project.room import Room
from project.hotel import Hotel

hotel = Hotel.from_stars(5)
room1 = Room(101, 3)
room2 = Room(102, 2)

hotel.add_room(room1)
hotel.add_room(room2)

print(hotel.status())

hotel.take_room(101, 2)
hotel.take_room(102, 2)

print(hotel.status())

hotel.free_room(101)
print(hotel.status())
