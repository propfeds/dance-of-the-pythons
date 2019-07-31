import tcod
from render_functions import RenderOrder

class Entity:
    def __init__(self, x, y, char, colour, name, hp, attack, shield, render_order=RenderOrder.CORPSE, pathable=True, ai=None, guard=None, item=None, inventory=None):
        self.x=x
        self.y=y
        self.char=char
        self.colour=colour
        self.name=name

        self.hp=hp
        self.max_hp=hp
        self.attack=attack
        self.shield=shield

        self.render_order=render_order
        self.pathable=pathable
        self.ai=ai
        self.guard=guard
        self.item=item
        self.inventory=inventory
        if self.ai:
            self.ai.owner=self
        # Used for enemy guards and wild animals. Guard attribute grants stats: stamina for patrolling duration (running away for tame animals), alertness
        if self.guard:
            self.guard.owner=self
        # Whether the entity is an item
        if self.item:
            self.item.owner=self
        # Whether the item has an inventory
        if self.inventory:
            self.inventory.owner=self
