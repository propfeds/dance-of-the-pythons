from data.enums import RenderOrder

class Graphics:
    def __init__(self, char, colour, render_order=RenderOrder.CORPSE):
        self.char=char
        self.colour=colour
        self.render_order=render_order