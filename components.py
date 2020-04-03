from snecs import RegisteredComponent, register_component

class Faction(RegisteredComponent):
    def __init__(self, id: int):
        self.id=id

class Health(RegisteredComponent):
    def __init__(self, capacity: int, regen_interval: int):
        self.capacity=capacity
        self.current=capacity
        self.regen_interval=regen_interval

class InputControlled(RegisteredComponent):
    def __init__(self):
        pass

# Contents: A list of item entities' IDs
class Inventory(RegisteredComponent):
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.contents=[]

# Display name is monster type: Snake, Soldier, Giant Dragonfly, etc.
# Given name is for locals or human plot characters
class Name(RegisteredComponent):
    def __init__(self, display: str, given: str=None):
        self.display=display
        if given is not None:
            self.given=given

class Position(RegisteredComponent):
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y

class Render(RegisteredComponent):
    def __init__(self, char: str, colour: str, order: str):
        self.char=char
        self.colour=colour
        self.order=order

class Stamina(RegisteredComponent):
    def __init__(self, capacity: int, sides: int, regen_interval: int):
        self.capacity=capacity
        self.sides=sides
        self.regen_interval=regen_interval
        self.reservoir=[]

class Velocity(RegisteredComponent):
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y
