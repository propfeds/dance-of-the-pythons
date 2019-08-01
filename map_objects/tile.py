class Tile:
    def __init__(self, char, colour_lit, colour_dim, name):
        self.char=char
        self.colour_lit=colour_lit
        self.colour_dim=colour_dim
        self.name=name
        self.explored=False
