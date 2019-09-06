from random import randint
from math import ceil
#pylint: disable=no-member

# Basic factory
def get_ai(ai):
    if ai.name=='none':         return None
    if ai.name=='guard':        return Guard(None)
    #if string=='reptile_body': return ReptileBody()
    if ai.name=='neutral_aggro':return NeutralAggro()   # snakes bears
    if ai.name=='neutral':      return Neutral()        # sometimes dogs, turns into aggro when provoked
    #if string=='neutral_tame': return NeutralTame()    # kripto the bunny
    
    return None

class Neutral:
    def take_turn(self, block_map, path_map):
        print('s')

class NeutralAggro:
    def take_turn(self, block_map, path_map):
        print('r')

class Guard:
    def __init__(self, target_entity=None):
        self.path=[]
        # target equals patrol point, but placeholder for now
        self.target_x=self.owner.x
        self.target_y=self.owner.y

        self.target_entity=target_entity
        if target_entity:
            self.target_x=target_entity.x
            self.target_y=target_entity.y

    def take_turn(self, spawner, path_map):
        results=[]
        # If target entity is in fov then chase, if not just stand still for now until something comes into range
        # Brute move: should favour diagonals
        dist=self.owner.distance(self.owner, self.target_x, self.target_y)
        dx=int(ceil(abs(self.target_x-self.owner.x)/dist))
        dy=int(ceil(abs(self.target_y-self.owner.y)/dist))
        results_movement=self.owner.handle_move(dx, dy, spawner, path_map, swappable=False)
        if results_movement==[]:
            print('Try A*, if not ten recalc A* and try again')
        results.extend(results_movement)
        return results