import tcod
from renderer import RenderOrder

class Entity:
    def __init__(self, x, y, name, faction, char, colour, hp, attack, shield, render_order=RenderOrder.CORPSE, walkable=True, inventory=None, item=None, ai=None, guard=None):
        self.x=x
        self.y=y
        self.name=name
        self.faction=faction
        self.char=char
        self.colour=colour

        self.hp=hp
        self.max_hp=hp
        self.attack=attack
        self.shield=shield

        self.render_order=render_order
        self.walkable=walkable
        self.guard=guard
        # Whether the entity has an inventory
        self.inventory=inventory
        if self.inventory:
            self.inventory.owner=self
        # Whether the entity is an item
        self.item=item
        if self.item:
            self.item.owner=self
        # Whether the entity has an AI (Not furniture)
        self.ai=ai
        if self.ai:
            self.ai.owner=self
        # Used for enemy guards and wild animals. (for detection)
        if self.guard:
            self.guard.owner=self

    def move(self, dx, dy):
        self.x+=dx
        self.y+=dy