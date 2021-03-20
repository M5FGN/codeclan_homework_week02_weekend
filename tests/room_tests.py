import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room('Pop Paradise', 30, 5.00)
    
    def test_room_has__name(self):
        self.assertEqual('Pop Paradise', self.room.room_name)

    def test_room_has__capacity(self):
        self.assertEqual(30, self.room.capacity)

    def test_room_has__fee(self):
        self.assertEqual(5.00, self.room.fee)