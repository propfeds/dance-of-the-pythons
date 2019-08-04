from enum import Enum
from renderer import RenderOrder
from entity import Entity

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

    def check_collision(self, x, y):
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
            self.entities.append('fuckoff')
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

    def spawn_item(self, x, y, entity_name):
        # Items can spawn beneath actors
        if not self.path_map.walkable[y, x]:
            return {'spawned': False}
        else:
            self.entities.append('fuckoff')
            return {'spawned': True}