from database import Database
from models import Room, Hotel, Booking, hotel
from collections import OrderedDict


class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        # Requirements:
        #   - Insert new hotel record into the database
        #   - Return a Hotel model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        return dict(reversed(list(self.db.hotels.insert(name = name).items())))

    def add_room(self, hotel_id, **params):
        # Requirements:
        #   - Insert new room record into the database
        #   - Return a Room model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        return self.db.rooms.insert(hotel_id = hotel_id, **params)

    def get_room(self, room_id):
        # Requirements:
        #   - Select a room with the room_id argument from the database
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
        if self.db.bookings.select(room_id = room_id) == []:
            return None
        return self.db.bookings.select(room_id = room_id)

    def book_room(self, room_id, **params):
        # Requirements:
        #   - Insert new booking record into the database
        #   - Return a Booking model by calling the model's create method instance with the query result

        # Remove the pass statement below and add your implementation there ...
        return self.db.bookings.insert(room_id = room_id, **params)

the_hotel= HotelSystem(Database)
print(the_hotel.register_hotel("Pearce Hotel"))
print(the_hotel.register_hotel("Raddison Blu"))
print(the_hotel.add_room(hotel_id= 1, price = 10000, capacity = 15))
print(the_hotel.add_room(hotel_id= 2, price = 8500, capacity = 10))
print(the_hotel.book_room(room_id =1, name = "Abiola", paid = True))
print(the_hotel.book_room(room_id =2, name = "Teniola", paid = False))
print(the_hotel.get_room(1))