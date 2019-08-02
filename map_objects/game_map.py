import tcod
import tcod.map
import numpy
import map_objects.generator as generator
from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        # path_map (class tcod.map.Map) holds pathability and sight, graphics_map holds graphical info
        self.width=width
        self.height=height
        self.path_map=tcod.map.Map(width, height, 'C')
        # Full of grass
        self.path_map.walkable[:]=True
        self.path_map.transparent[:]=True
        self.graphics_map=numpy.full((height, width), Tile('•', (106, 190, 48), (57, 60, 50)))
        self.explored=numpy.full((height, width), False)
        origin_x=3
        dest_x=generator.cave_y(origin_x, 0, 21, Tile('•', (138, 111, 48), (82, 75, 36)), 60, 60, 1, 1, self)

    def recompute_fov(self, x, y, radius, light_walls, algorithm):
        self.path_map.compute_fov(x, y, radius, light_walls, algorithm)