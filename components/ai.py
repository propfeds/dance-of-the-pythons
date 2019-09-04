from random import randint
from math import ceil
from spawner import Factions
#pylint: disable=no-member

# Basic factory
def get_ai(ai):
    if ai.name=='guard':         return Guard(None)          # only enemy
    #if string=='reptile_body':  return ReptileBody()
    if ai.name=='neutral_aggro': return NeutralAggro()   # snakes bears
    if ai.name=='neutral':       return Neutral()        # sometimes dogs, turns into aggro when provoked
    #if string=='neutral_tame':  return NeutralTame()    # kripto the bunny
    
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
        # Try brute move, then try a*, if not recalculate a* and try again
        dist=self.owner.distance(self.owner, self.target_x, self.target_y)
        dx=int(ceil(abs(self.target_x-self.owner.x)/dist))
        dy=int(ceil(abs(self.target_y-self.owner.y)/dist))

        # RESULTS EXTEND
        response=spawner.check_collision(self.owner.x+dx, self.owner.y+dy, path_map)
        target=response.get('collide')
        if target:
            if target.faction==self.owner.faction or target.faction==Factions.NEUTRAL:
                # try a* if not recalc
                print('Geddout my way binch! Cursed thee {0}!'.format(target.name))
            else:
                print('KILL')   #RESULTS EXTEND
        elif (not response.get('blocked')) and (not response.get('outofbounds')):
            self.owner.move(dx, dy, spawner.block_map)
        return results