from random import randint
#pylint: disable=no-member

# Basic factory
def get_ai(string):
    if string=='guard':         return Guard()          # only enemy
    #if string=='reptile_body':  return ReptileBody()
    if string=='neutral_aggro': return NeutralAggro()   # snakes bears
    if string=='neutral':       return Neutral()        # sometimes dogs, turns into aggro when provoked
    #if string=='neutral_tame':  return NeutralTame()    # kripto the bunny
    
    return None

class Neutral:
    def take_turn(self, block_map, path_map):
        print('s')

class NeutralAggro:
    def take_turn(self, block_map, path_map):
        print('r')

class Guard:
    def take_turn(self, spawner, path_map):
        results=[]
        dx=randint(-1, 1)
        dy=randint(-1, 1)
        # RESULTS EXTEND
        response=spawner.check_collision(self.owner.x+dx, self.owner.y+dy)
        target=response.get('collide')
        if target:
            if target.faction==self.owner.faction:
                print('Geddout my way binch! Cursed thee {0}!'.format(target.name))
            else:
                print('KILL')   #RESULTS EXTEND
        elif (not response.get('blocked')) and (not response.get('outofbounds')):
            self.owner.move(dx, dy, spawner.block_map)
        return results