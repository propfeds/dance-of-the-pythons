class Offence:
    def __init__(self, damage, to_hit=0, piercing=False, lethal=True):
        # To hit is a bonus
        self.damage=damage
        self.to_hit=to_hit
        # Piercing means to penetrate overshield
        self.piercing=piercing
        self.lethal=lethal