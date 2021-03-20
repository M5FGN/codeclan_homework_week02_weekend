import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song('0001', 'Nickleback', 'Faraway')

    def test_song_has__song_number(self):
        self.assertEqual('0001', self.song.song_number)

    def test_song_has__artist(self):
        self.assertEqual('Nickleback', self.song.artist)

    def test_song_has__title(self):
        self.assertEqual('Faraway', self.song.song_title)