from data.enums import RenderOrder
from json import load
from random import randint

with open('data/constants.json', 'r') as json_constants:
    constants=load(json_constants)

class Defence:
    def __init__(self, health_max, ac=0, to_hit=0):
        self.health_max=health_max
        self.health=health_max
        self.ac=ac
        # To hit is a bonus
        self.to_hit=to_hit

class Die:
    def __init__(self, dice=1, sides=20, mod=0):
        self.dice=dice
        self.sides=sides
        self.mod=mod

    def roll(self):
        result=self.mod
        for _ in range(self.dice):
            result+=randint(1, self.sides)
        return result

    @property
    def roll_min(self):
        return self.dice+self.mod

    @property
    def roll_max(self):
        return self.dice*self.sides+self.mod

    @property
    def roll_average(self):
        return ((float(self.roll_min)+float(self.roll_max))/2.0)

    def __str__(self):
        die_format=''
        if self.dice!=1:
            die_format+=str(self.dice)
        die_format+='d{0}'.format(self.sides)
        if self.mod!=0:
            if self.mod>0:
                die_format+='+'
            die_format+=str(self.mod)
        return die_format

class Faction:
    def __init__(self, faction):
        self.faction=faction

class Graphics:
    def __init__(self, char, colour, render_order=RenderOrder.ENVIRONMENT):
        self.char=char
        self.colour=colour
        self.render_order=render_order

class Identity:
    def __init__(self, display_name, given_name=None):
        # Name is monster type: Snake, Soldier, etc.
        # Given name is for fellow tribesmen or plot characters
        self.display_name=display_name
        self.given_name=given_name

class InputControlled:
    def __init__(self):
        pass

class Inventory:
    def __init__(self, capacity):
        self.capacity=capacity
        self.contents=[]

class Movement:
    def __init__(self, walkable, swappable=False, cost=constants['default_movement_cost'], hover=False):
       self.walkable=walkable
       self.swappable=swappable
       self.cost=cost
       # Hover: a bool indicating hovering status
       self.hover=hover

class Offence:
    def __init__(self, damage, to_hit=0, piercing=False, lethal=True):
        # To hit is a bonus
        self.damage=damage
        self.to_hit=to_hit
        # Piercing means to penetrate overshield
        self.piercing=piercing
        self.lethal=lethal

class Position:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def displace(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def swap(self, target_entity):
        x_temp=self.x
        y_temp=self.y
        self.x=target_entity.components[Position].x
        self.y=target_entity.components[Position].y
        target_entity.components[Position].x=x_temp
        target_entity.components[Position].y=y_temp

class Vision:
    def __init__(self, block=False, fov_radius=constants['default_fov_radius'], fov_radius_dark=constants['default_fov_radius_dark']):
        self.block=block
        self.fov_radius=fov_radius
        self.fov_radius_dark=fov_radius_dark
        self.fov_recompute=True

