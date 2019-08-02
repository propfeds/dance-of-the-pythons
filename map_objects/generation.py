import tcod
from map_objects.tile import Tile

def init_grass(game_map):
    game_map.path_map.walkable[:]=True
    game_map.path_map.transparent[:]=True
    game_map.graphics_map=[[Tile('.', tcod.light_green, tcod.darker_green, 'Grass') for x in range(game_map.width)] for y in range(game_map.height)]