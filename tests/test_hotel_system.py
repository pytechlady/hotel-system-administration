from unittest import TestCase
from hotel_system import HotelSystem
from database import Database, Table

class TestHotelSystem(TestCase):

    def setUp(self):
        self.hotel_system = HotelSystem(db={Table})

    def test_register_room(self):
        self.assertTrue(self.hotel_system.register_hotel, True)
    
    def test_add_room(self):
        self.assertTrue(self.hotel_system.add_room, True)

    def test_get_room(self):
        self.assertNotEqual(self.hotel_system.get_room, {})
    
    def test_book_room(self):
        self.assertIsNotNone(self.hotel_system.book_room)
    
    def test_register_hotel(self):
        self.assertIsNotNone(self.hotel_system.register_hotel)
    
    def tearDown(self):
        self.hotel_system = HotelSystem(db={Table})
        print("Man down")