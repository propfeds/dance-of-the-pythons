from data.enums import Factions

class Identity:
    def __init__(self, display_name, given_name=None):
        # Name is monster type: Snake, Soldier, etc.
        # Given name is for fellow tribesmen or plot characters
        self.display_name=display_name
        self.given_name=given_name