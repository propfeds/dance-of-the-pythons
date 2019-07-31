class Tile:
    def __init__(self, name, pathable, transparent):
        self.name=name
        self.pathable=pathable
        self.transparent=transparent
        self.explored=False
