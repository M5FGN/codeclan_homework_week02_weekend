import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestGuest(unittest.TestCase):

# Testing that classes have been Setup OK
    
    def setUp(self):

        self.song_1 = Song('S001', 'Nickleback', 'Faraway')
        self.song_2 = Song('S002', 'The Weekend', 'Save Your Tears')
        self.song_3 = Song('S003', 'Daxten', 'Somewhere Out There')

        playlist_1 = [self.song_1, self.song_2]

        self.guest_1 = Guest('Joey Tribbiani', 100.00, 'Entrance Hallway', 'S001')
        self.guest_2 = Guest('Ross Gellar', 75.00, 'Entrance Hallway', 'S002')
        self.guest_3 = Guest('Chandler Bing', 50.00, 'Pop Paradise', 'S002')

        current_visitors_1 = [self.guest_1,  self.guest_2]

        self.room = Room('Pop Paradise', 30, 5.00, 0.00, current_visitors_1, playlist_1)

    def test_guest_has__guest_name(self):
        self.assertEqual('Joey Tribbiani', self.guest_1.guest_name)

    def test_guest_has__wallet(self):
        self.assertEqual(100.00, self.guest_1.wallet)

    def test_guest_has__current_room(self):
        self.assertEqual('Entrance Hallway', self.guest_1.current_room)

    def test_guest_has__favourite_song(self):
        self.assertEqual('S001', self.guest_1.favourite_song)

# Testing Methods needed for adding guest to a room

    # Advanced Check-in/out

    def test_guest__can_afford_fee_high_wallet(self):
        self.assertEqual(True, self.guest_1.check_affordabilty(self.room.fee))

    def test_guest__can_afford_fee_low_wallet(self):
        guest_low_wallet = Guest('Gunther', 0.00, 'Entrance Hallway', 'S005')
        self.assertEqual(False, guest_low_wallet.check_affordabilty(self.room.fee))
    
    def test_guest__can_afford_fee_exact_wallet(self):
        guest_exact_wallet = Guest('Gunther', 5.00, 'Entrance Hallway','S005')
        self.assertEqual(True, guest_exact_wallet.check_affordabilty(self.room.fee))

    def test_pay_fee(self):
        self.assertEqual(95.00, self.guest_1.pay_fee(self.room.fee))
        self.assertEqual(70.00, self.guest_2.pay_fee(self.room.fee))
        self.assertEqual(45.00, self.guest_3.pay_fee(self.room.fee))

    def test_set_current_room(self):
        self.assertEqual('Pop Paradise', self.guest_1.set_room('Pop Paradise'))

