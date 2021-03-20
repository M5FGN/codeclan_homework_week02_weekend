import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest('G001', 'Joey Tribbiani', 100.00)

    def test_guest_has__guest_number(self):
        self.assertEqual('G001', self.guest.guest_number)

    def test_guest_has__guest_name(self):
        self.assertEqual('Joey Tribbiani', self.guest.guest_name)

    def test_guest_has__wallet(self):
        self.assertEqual(100.00, self.guest.wallet)
    