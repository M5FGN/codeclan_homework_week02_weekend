import pdb

class Room:

# Define Class
    
    def __init__(self, room_name, capacity, fee, total_income, current_visitors, playlist):
        self.room_name = room_name
        self.capacity = capacity
        self.fee = fee
        self.total_income = total_income 
        self.current_visitors = current_visitors
        self.playlist = playlist

# Add song to playlist

    def add_song_to_playlist(self, new_song):
        self.playlist.append(new_song)

# Methods needed for guests entering and leaving rooms

    # Basic Check-in/out 

    def basic_checkin(self, in_guest):
        self.current_visitors.append(in_guest)

    def basic_checkout(self, out_guest):
        self.current_visitors.remove(out_guest)


    # Advanced Check-in/out

    # - Needed to check against room capacity

    def count_visitors(self):
        return len(self.current_visitors)
    

    # - To collect Fee

    def collects_fee(self, fee):
        self.total_income += fee
        return self.total_income

    #- Advanced Checkin in one method

    def advanced_checkin(self, in_guest, fee):
        # pdb.set_trace()
        # Check to see if guest can afford room fee
        # If yes:
            # self.add_guest_to_room(new_guest)
            # Check room is under capacity
            # If Yes:
                # Room collects fee/guest pays fee
                # Guest added to room
        # If no:
        # Guest remains in entrance hallway
        # return len(self.current_visitors)
        pass


    def advanced_checkout(self):
        # Guest current_room set to Entrance Hallway
        # Guest is removed from the x room list and added to entrance hallway
        pass

#  Method needed to check for guest favourite song.

    def check_favourite(self, guest_favourite_song):
        favourite_found = 'Sad'
        for song in self.playlist:
            if song.song_number == guest_favourite_song:
                favourite_found = 'Woo!'
        return favourite_found