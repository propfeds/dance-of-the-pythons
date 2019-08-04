import json
from enum import Enum
from renderer import RenderOrder
from entity import Entity
from components.inventory import Inventory

class Factions(Enum):
    NEUTRAL=0
    ALLY=1
    ENEMY=2

class Spawner:
    def __init__(self, width, height, level, path_map):
        self.width=width
        self.height=height
        self.level=level
        self.path_map=path_map
        self.entities=[]
        # Loading data
        with open('data/items.json') as data:
            self.data_items=json.load(data)
        with open('data/environment.json') as data:
            self.data_environment=json.load(data)
        with open('data/furniture.json') as data:
            self.data_furniture=json.load(data)
        with open('data/actors.json') as data:
            self.data_actors=json.load(data)

        with open('gfx/colours/items.json', encoding='utf-8') as gfx:
            self.gfx_items=json.load(gfx)
        with open('gfx/colours/environment.json', encoding='utf-8') as gfx:
            self.gfx_environment=json.load(gfx)
        with open('gfx/colours/furniture.json', encoding='utf-8') as gfx:
            self.gfx_furniture=json.load(gfx)
        with open('gfx/colours/actors.json', encoding='utf-8') as gfx:
            self.gfx_actors=json.load(gfx)
        

    def check_collision(self, x, y):
        # Colliding with the offworld
        if x<0 or y<0 or x>=self.width or y>=self.height:
            return True
        if not self.path_map.walkable[y, x]:
            return True
        for entity in self.entities:
            if entity.x==x and entity.y==y:
                return True
        return False

    def spawn_ally(self, x, y, entity_name):
        if self.check_collision(x, y):
            return {'spawned': False}
        else:
            entity=Entity(x, y, entity_name, Factions.ALLY, self.gfx_actors[entity_name]['char'], tuple(self.gfx_actors[entity_name]['colour']), self.data_actors[entity_name]['hp_max'], self.data_actors[entity_name]['attack'], self.data_actors[entity_name]['shield'], self.data_actors[entity_name]['alert_threshold'], RenderOrder.ACTOR, self.data_actors[entity_name]['walkable'], Inventory(self.data_actors[entity_name]['inventory_capacity']), (None if (entity_name=='player') else self.data_actors[entity_name]['ai']))
            self.entities.append()
            return {'spawned': True}

    def spawn_enemy(self, x, y, entity_name):
        if self.check_collision(x, y):
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}

    def spawn_neutral(self, x, y, entity_name):
        if self.check_collision(x, y):
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}

    def spawn_furniture(self, x, y, entity_name):
        if self.check_collision(x, y):
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}

    def spawn_item(self, x, y, entity_name, item_component):
        # Items can spawn beneath actors
        if not self.path_map.walkable[y, x]:
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}

    def spawn_environment(self, x, y, environment_component):
        # Environment entities can spawn beneath actors
        if not self.path_map.walkable[y, x]:
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}