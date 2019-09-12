class Defence:
    def __init__(self, max_health, ac=0, to_hit=0):
        self.max_health=max_health
        self.health=max_health
        self.ac=ac
        # To hit is a bonus
        self.to_hit=to_hit