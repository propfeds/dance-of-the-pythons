class Defence:
    def __init__(self, health_max, ac=0, to_hit=0):
        self.health_max=health_max
        self.health=health_max
        self.ac=ac
        # To hit is a bonus
        self.to_hit=to_hit