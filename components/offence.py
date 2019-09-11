class Offence:
    def __init__(self, damage, to_hit=0):
        # To hit is a bonus
        self.damage=damage
        self.to_hit=to_hit