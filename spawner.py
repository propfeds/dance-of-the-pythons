import json
import numpy
from components.ai import get_ai
from enums import RenderOrder
from entity import Entity
from components.inventory import Inventory


class Spawner:
    def __init__(self, width, height, level):
        self.width=width
        self.height=height
        self.level=level
        # Path map is terrain blockade, block map is entity blockade
        self.block_map=numpy.full((height, width), False)
        self.entities=[]
        # Loading data
        with open('data/entities.json') as data:
            self.entity_data=json.load(data)
        with open('gfx/colours/entities.json', encoding='utf-8') as gfx:
            self.entity_gfx=json.load(gfx)
        with open('gfx/colours/palette.json') as colours:
            self.palette=json.load(colours)
        

    def check_collision(self, x, y, path_map):
        # Colliding with the offworld
        if x<0 or y<0 or x>=self.width or y>=self.height:
            return {'outofbounds': True}
        if not path_map.walkable[y, x]:
            return {'blocked': True}
        if self.block_map[y, x]:
            for entity in self.entities:
                if entity.x==x and entity.y==y and (not entity.walkable):
                    return {'collide': entity}
        return {}

    def spawn_actor(self, x, y, entity_name, faction, path_map):
        if self.check_collision(x, y, path_map):
            return {'spawned': False}
        else:
            # If short you can walk through ;)
            short=self.entity_data['actors'][entity_name]['walkable']
            char=self.entity_gfx['actors'][entity_name]['char']
            colour=tuple(self.palette[self.entity_gfx['actors'][entity_name]['colour']])
            hp_max=self.entity_data['actors'][entity_name]['hp_max']
            attack=self.entity_data['actors'][entity_name]['attack']
            shield=self.entity_data['actors'][entity_name]['shield']
            alert_threshold=self.entity_data['actors'][entity_name]['alert_threshold']
            inventory_component=Inventory(self.entity_data['actors'][entity_name]['inventory_capacity'])
            ai_component=get_ai(self.entity_data['actors'][entity_name]['ai'])
            
            entity=Entity(x, y, entity_name, faction, char, colour, hp_max, attack, shield, alert_threshold, (RenderOrder.ACTOR_SHORT if short else RenderOrder.ACTOR), short, inventory_component, ai_component)
            self.entities.append(entity)
            self.block_map[y, x]=(not short)
            return {'spawned': True}

    def spawn_furniture(self, x, y, entity_name, path_map):
        if self.check_collision(x, y, path_map):
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}

    def spawn_item(self, x, y, entity_name, item_component, path_map):
        # Items can spawn beneath actors (don't need to check entity collision)
        if not path_map.walkable[y, x]:
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}

    def spawn_environment(self, x, y, environment_component, path_map):
        # Environment entities like smoke can spawn beneath actors (don't need to check entity collision)
        if not path_map.walkable[y, x]:
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}