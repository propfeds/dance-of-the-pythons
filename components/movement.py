class Movement:
    def __init__(self, x, y, walkable=True, speed=100, hover=False):
       self.x=x
       self.y=y
       self.walkable=walkable
       self.speed=speed
       # Hover: a bool indicating hovering status
       self.hover=hover