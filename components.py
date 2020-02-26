import esper

class Faction:
    def __init__(self, name: str):
        self.name=name

class Graphics:
    def __init__(self, char: str, colour: str, render_order: str):
        self.char=char
        self.colour=colour
        self.render_order=render_order

class InputControlled:
    def __init__(self):
        pass

# Contents: A list of item entities' IDs
class Inventory:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.contents=[]

class Position:
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y

class Velocity:
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y
