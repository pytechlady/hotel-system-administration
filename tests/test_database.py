from unittest import TestCase
from database import Table


class TestDatabase(TestCase):

    def setUp(self):
        self.database = Table()
    
    def test_table(self):
        self.assertIsNotNone(self.database.insert)

    def test_table_insert(self):
        self.assertTrue(self.database.insert, True)

    def test_table_select(self):
        self.assertIsNotNone(self.database.select)

    def test_table_select_true(self):
        self.assertTrue(self.database.select, True)

    def test_table_db(self):
        self.assertNotEqual(self.database.select, {})
        
    def tearDown(self):
        self.database = Table()
        print("Ending test")