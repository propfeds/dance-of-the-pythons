import tcod
import tcod.map
from map_objects.generation import init_grass

class GameMap:
    def __init__(self, width, height):
        # path_map (class tcod.map.Map) holds pathability and sight, graphics_map holds graphical info
        self.width=width
        self.height=height
        self.path_map=tcod.map.Map(width, height, 'C')
        self.graphics_map=[[]]
        # Full of grass
        init_grass(self)

    def recompute_fov(self, x, y, radius, light_walls, algorithm):
        self.path_map.compute_fov(x, y, radius, light_walls, algorithm)