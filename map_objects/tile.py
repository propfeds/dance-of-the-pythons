class Tile:
    def __init__(self, char, colour, name, pathable, transparent):
        self.char=char
        self.colour=colour
        self.name=name
        self.pathable=pathable
        self.transparent=transparent
        self.explored=False
