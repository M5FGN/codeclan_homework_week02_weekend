import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):

# Testing that classes have been Setup OK

    def setUp(self):
        self.song_1 = Song('S001', 'Nickleback', 'Faraway')
        self.song_2 = Song('S002', 'The Weekend', 'Save Your Tears')
        self.song_3 = Song('S003', 'Daxten', 'Somewhere Out There')

    def test_song_has__song_number(self):
        self.assertEqual('S001', self.song_1.song_number)
        self.assertEqual('S002', self.song_2.song_number)
        self.assertEqual('S003', self.song_3.song_number)

    def test_song_has__artist(self):
        self.assertEqual('Nickleback', self.song_1.artist)
        self.assertEqual('The Weekend', self.song_2.artist)
        self.assertEqual('Daxten', self.song_3.artist)

    def test_song_has__title(self):
        self.assertEqual('Faraway', self.song_1.song_title)
        self.assertEqual('Save Your Tears', self.song_2.song_title)
        self.assertEqual('Somewhere Out There', self.song_3.song_title)

    