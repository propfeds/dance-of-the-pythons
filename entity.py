import tcod
from renderer import RenderOrder

class Entity:
    def __init__(self, x, y, name, faction, char, colour, hp_max, attack, shield, alert_threshold, render_order=RenderOrder.CORPSE, walkable=True, inventory=None, ai=None, item=None, environment=None):
        self.x=x
        self.y=y
        self.name=name
        self.faction=faction
        self.char=char
        self.colour=colour

        self.hp_max=hp_max
        self.hp=hp_max
        self.attack=attack
        self.shield=shield
        self.alert_threshold=alert_threshold
        self.alert=0

        self.render_order=render_order
        # Is pathable and not the ability to walk
        self.walkable=walkable
        # Whether the entity has an inventory, is an item or has an AI (if not then furniture)
        self.inventory=inventory
        if self.inventory:
            self.inventory.owner=self
        self.ai=ai
        if self.ai:
            self.ai.owner=self
        self.item=item
        if self.item:
            self.item.owner=self
        self.environment=environment
        if self.environment:
            self.environment.owner=self

    def move(self, dx, dy, block_map):
        if not self.walkable:
            block_map[self.y, self.x]=False
        self.x+=dx
        self.y+=dy
        if not self.walkable:
            block_map[self.y, self.x]=(not self.walkable)

    def swap(self, target):
        x=self.x
        y=self.y
        self.x=target.x
        self.y=target.y
        target.x=x
        target.y=y
        return {'swap': target}