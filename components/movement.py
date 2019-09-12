class Movement:
    def __init__(self, walkable, swappable=False, speed=100, hover=False):
       self.walkable=walkable
       self.swappable=swappable
       self.speed=speed
       # Hover: a bool indicating hovering status
       self.hover=hover