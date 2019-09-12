class Movement:
    def __init__(self, x, y, walkable, swappable=False, speed=100, hover=False):
       self.x=x
       self.y=y
       self.walkable=walkable
       self.swappable=swappable
       self.speed=speed
       # Hover: a bool indicating hovering status
       self.hover=hover