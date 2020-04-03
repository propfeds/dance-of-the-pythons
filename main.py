import tcod
from snecs import World, new_entity()

def main():
    world=World(name='dotp')
    player_id=new_entity(world=world)

if __name__=='__main__':
    main()