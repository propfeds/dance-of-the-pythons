class Tile:
    def __init__(self, name, char, colour, pathable, transparent):
        self.name=name
        self.char=char
        self.colour=colour
        self.pathable=pathable
        self.transparent=transparent
        self.explored=False
