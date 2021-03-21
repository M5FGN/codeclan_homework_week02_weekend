import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

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

    def test_room_has__name(self):
        self.assertEqual('Pop Paradise', self.room.room_name)

    def test_room_has__capacity(self):
        self.assertEqual(30, self.room.capacity)

    def test_room_has__fee(self):
        self.assertEqual(5.00, self.room.fee)

    def test_room_has__total_income(self):
        self.assertEqual(0, self.room.total_income)

    def test_room_has__visitors(self):
        self.assertEqual(2, len(self.room.current_visitors))

    def test_room_has_playlist(self):
        self.assertEqual(2, len(self.room.playlist))

#  Testing Methods to add song to playlist

    def test_adding_song_to_a_playlist(self):
        self.room.add_song_to_playlist(self.song_3)
        self.assertEqual(3, len(self.room.playlist))

# Testing Methods needed for guests entering and leaving rooms

    # Basic Check-in/out 

    def test_basic_checkin(self):
        self.room.basic_checkin(self.guest_3)
        self.assertEqual(3, len(self.room.current_visitors))

    def test_basic_checkin(self):
        self.room.basic_checkout(self.guest_1)
        self.assertEqual(1, len(self.room.current_visitors))

    # Advanced Check-in/out

    def test_count_guests(self):
        self.assertEqual(2, self.room.count_visitors())    

    def test_room_can_take_fee(self):
        self.assertEqual(5.00, self.room.collects_fee(self.room.fee))

    # def test_advanced_checkin(self):
        # Add test here

    # def test_advanced_checkout(self):
        # Add test here


#  Test Method needed to check for guest favourite song.

    def test_check_favourite(self):
        self.assertEqual('Woo!', self.room.check_favourite(self.guest_3.favourite_song))
