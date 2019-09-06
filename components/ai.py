from random import randint
from math import ceil
#pylint: disable=no-member

# Basic factory
def get_ai(ai):
    if ai==None:
        return None

    name=ai.get('name')
    if name=='guard':           return Guard()
    #elif name=='reptile_body': return ReptileBody()
    elif name=='neutral_aggro': return NeutralAggro()
    elif name=='neutral':       return Neutral()    # Turns into aggro when provoked
    #elif name=='neutral_tame': return NeutralTame()

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
        self.target_x=0
        self.target_y=0

        self.target_entity=target_entity
        if target_entity:
            self.set_target(target_entity)

    def set_target(self, target_entity):
        self.target_x=target_entity.x
        self.target_y=target_entity.y

    def take_turn(self, spawner, path_map):
        results=[]
        # If target entity is in fov then chase, if not just stand still for now until something comes into range
        # Brute move: should move in a rough line
        dist=self.owner.distance(self.target_x, self.target_y)
        dx=int(round(self.target_x-self.owner.x)/dist) if dist>0 else 0
        dy=int(round(self.target_y-self.owner.y)/dist) if dist>0 else 0
        results_movement=self.owner.handle_move(dx, dy, spawner, path_map, swappable=False)
        if results_movement==[]:
            print('Try A*, if not then recalc A* and try again')
        results.extend(results_movement)
        return results