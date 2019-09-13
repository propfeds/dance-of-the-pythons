class Movement:
    def __init__(self, walkable, swappable=False, cost=100, hover=False):
       self.walkable=walkable
       self.swappable=swappable
       self.cost=cost
       # Hover: a bool indicating hovering status
       self.hover=hover