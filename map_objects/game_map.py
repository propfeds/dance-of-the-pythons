import tcod
import tcod.map
import numpy
import json
from random import randint
from map_objects.tile import Tile
from map_objects.rectangle import Rectangle

class GameMap:
    def __init__(self, width, height):
        # path_map (class tcod.map.Map) holds pathability and sight, graphics holds graphical info
        self.width=width
        self.height=height
        # The void
        self.path_map=tcod.map.Map(width, height, 'C')
        self.graphics=numpy.full((height, width), Tile(' ', (0, 0, 0), (0, 0, 0)))
        self.destructible=numpy.full((height, width), False)
        self.explored=numpy.full((height, width), False)
        # Importing tiles data (please only load at level 1)
        with open('data/tiles.json', encoding='utf-8') as data:
            self.tile_data=json.load(data)
        with open('gfx/colours/tiles.json', encoding='utf-8') as gfx:
            self.tile_gfx=json.load(gfx)
        # Test: Full of grass
        self.fill_rect(Rectangle(0, 0, width, height), 'ground_grass')
        x_dest=self.cave_y(5, 0, self.height-6, 'ground_dirt', 35, 50, 1, 1, 3)
        x_dest=self.cave_y(5, 0, self.height-1, 'ground_dirt', 100, 100, 1, 0, 2)
        self.fill_rect(Rectangle(3, self.height-8, 5, 5), 'wall_tent')
        self.fill_rect(Rectangle(5, self.height-8, 1, 1), 'wall_tent_window')
        self.fill_rect(Rectangle(4, self.height-7, 3, 3), 'ground_dirt')
        x_dest=self.cave_y(21, 0, self.height-7, 'wall_tree', 78, 78, 1, 3, 5)
        y_dest=self.cave_x(13, 0, self.width-30, 'wall_dirt', 15, 15, 1, 1, 2)

    def recompute_fov(self, x, y, radius, light_walls, algorithm):
        self.path_map.compute_fov(x, y, radius, light_walls, algorithm)
    
    def fill_rect(self, rect, tile_name):
        self.graphics[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=Tile(self.tile_gfx[tile_name]['char'], tuple(self.tile_gfx[tile_name]['colour_lit']), tuple(self.tile_gfx[tile_name]['colour_dim']))
        self.path_map.walkable[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.tile_data[tile_name]['walkable']
        self.path_map.transparent[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.tile_data[tile_name]['transparent']
        self.destructible[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.tile_data[tile_name]['destructible']

    # www.roguebasin.com/index.php?title=Basic_directional_dungeon_generation
    # Pretty useful, can be used for caves, beaten paths (straight paths would be pretty slow I tell ya), rivers, etc
    # tile: fills the entire path with it
    # roughness (0~100%): how often the path changes in width throughout the journey
    # wind (0~100%): how often the path changes in left border
    # swole: how big of a change the path can get
    # width_min/max: how small/big it could get

    def cave_y(self, x_origin, y_origin, y_dest, tile_name, roughness, wind, swole, width_min, width_max):
        # step determines whether the algo runs up or down
        step=1
        if(y_origin>y_dest):
            step=-1
        width_current=width_min
        x_current=x_origin
        for y in range(y_origin, y_dest+step, step):
            roll_rough=randint(0, 100)
            if roll_rough<roughness:
                width_current=max(width_min, width_current+randint(-swole, swole))
                width_current=min(width_current, width_max)
            if y!=y_origin:
                wind_roll=randint(0, 100)
                if wind_roll<wind:
                    x_current=max(0, x_current+randint(-swole, swole))
                    x_current=min(x_current, self.width-width_min)
            self.fill_rect(Rectangle(x_current, y, width_current, 1), tile_name)
            # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
        # Returns x_current because it's the end of the road (level transitions/'stairs')
        return x_current

    def cave_x(self, y_origin, x_origin, x_dest, tile_name, roughness, wind, swole, height_min, height_max):
        # step determines whether the algo runs up or down
        step=1
        if(x_origin>x_dest):
            step=-1
        height_current=height_min
        y_current=y_origin
        for x in range(x_origin, x_dest+step, step):
            roll_rough=randint(0, 100)
            if roll_rough<roughness:
                height_current=max(height_min, height_current+randint(-swole, swole))
                height_current=min(height_current, height_max)
            if x!=x_origin:
                wind_roll=randint(0, 100)
                if wind_roll<wind:
                    y_current=max(0, y_current+randint(-swole, swole))
                    y_current=min(y_current, self.height-height_min)
            self.fill_rect(Rectangle(x, y_current, 1, height_current), tile_name)
            # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
        # Returns x_current because it's the end of the road (level transitions/'stairs')
        return y_current

    