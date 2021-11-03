from unittest import TestCase
from models import Booking, Hotel, Room

class TestModels(TestCase):

    def setUp(self):
        self.booking = Booking()
        self.hotel = Hotel()
        self.room = Room() 

    def test_hotel(self):
        self.assertIsNotNone(self.hotel.create)

    def test_room(self):
        self.assertIsNotNone(self.room.create)
        
    def test_hotel_room(self):
        self.assertIsNotNone(self.room.hotel)
    
    def test_booking(self):
        self.assertIsNotNone(self.booking.create)
        
    def test_room_booking(self):
        self.assertIsNotNone(self.booking.room)

    def tearDown(self):
        self.booking = Booking()
        self.hotel = Hotel()
        self.room = Room() 
        print("Tearing down test")
