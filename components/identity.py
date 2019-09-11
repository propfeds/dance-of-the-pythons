from data.enums import Factions

class Identity:
    def __init__(self, name, given_name=None, faction=None):
        # Name is monster type: Snake, Soldier, etc.
        # Given name is for fellow tribesmen or plot characters
        self.name=name
        self.given_name=given_name
        self.faction=faction