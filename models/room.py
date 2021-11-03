from .model import Model
from .hotel import Hotel
from models import hotel


class Room(Model):
    _id = None
    hotel_id = None
    price = None
    capacity = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes

        instance = cls()
        instance._id = record["_id"]
        instance.hotel_id = record["hotel_id"]
        instance.price = record.get["price"]
        instance.capacity = record["capacity"]
        return instance

    def hotel(self, db):
        #select where self.hotel_id == db.get(hotel_id)
        # Requirements:
        #   - Select hotels from the database that has the hotel_id set on this model as self.hotel_id
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Hotel model instance by calling the model's create method with the first record in the query results

        # Remove the pass statement below and add your implementation there ...
        hotel_name = db.hotel.select(_id = self.hotel_id)
        if len(hotel_name) == 0:
            return None
        else:
            return Hotel.create(hotel_name)

