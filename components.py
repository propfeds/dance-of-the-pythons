
class Faction:
    def __init__(self, name: str):
        self.name=name

class Health:
    def __init__(self, capacity: int, regen_interval: int):
        self.capacity=capacity
        self.current=capacity
        self.regen_interval=regen_interval

class InputControlled:
    def __init__(self):
        pass

# Contents: A list of item entities' IDs
class Inventory:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.contents=[]

# Display name is class or monster type: Snake, Soldier, Giant Dragonfly, etc.
# Given name is for locals or human plot characters
class Name:
    def __init__(self, display: str, given: str=None):
        self.display=display
        if given is not None:
            self.given=given

class Position:
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y

class Render:
    def __init__(self, char: str, colour: str, order: str):
        self.char=char
        self.colour=colour
        self.order=order

class Stamina:
    def __init__(self, capacity: int, sides: int, regen_interval: int):
        self.capacity=capacity
        self.sides=sides
        self.regen_interval=regen_interval
        self.reservoir=[]

class Velocity:
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y
