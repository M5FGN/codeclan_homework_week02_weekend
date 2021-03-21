class Guest:
    
    def __init__(self, guest_name, wallet, current_room, favourite_song):
        self.guest_name = guest_name
        self.wallet = wallet
        self.current_room = current_room
        self.favourite_song = favourite_song

# Methods needed for guests entering and leaving rooms

    # Advanced Check-in/out

    # - Checks guest has enough money for the room fee

    def check_affordabilty(self, fee):
        if self.wallet >= fee:
            return True
        else: 
            return False 

    # - Pays the room fee

    def pay_fee(self, fee):
        self.wallet -= fee 
        return self.wallet

    # - Changes the guests current room
    
    def set_room(self, new_room):
        self.current_room = new_room
        return self.current_room

