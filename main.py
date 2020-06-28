from data.entities import spawn_player
from snecs import World
import tcod

def main():
    world=World(name='dotp')
    player_id=spawn_player(world, 0, 0)

if __name__=='__main__':
    main()