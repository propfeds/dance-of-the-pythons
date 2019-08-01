import tcod
import tcod.map
from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        # path_map (class tcod.map.Map) holds pathability and sight, graphics_map holds graphical info
        self.width=width
        self.height=height
        # Full of grass
        self.path_map=tcod.map.Map(width, height, 'C')
        self.path_map.walkable[:]=True
        self.path_map.transparent[:]=True
        self.graphics_map=[[Tile('.', tcod.light_green, tcod.dark_green, 'Grass') for x in range(self.width)] for y in range(self.height)]

    def recompute_fov(self, x, y, radius, light_walls, algorithm):
        self.path_map.compute_fov(x, y, radius, light_walls, algorithm)