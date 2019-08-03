import tcod
import tcod.map
import numpy
import json
from random import randint
from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        # path_map (class tcod.map.Map) holds pathability and sight, graphics_map holds graphical info
        self.width=width
        self.height=height
        self.path_map=tcod.map.Map(width, height, 'C')
        # Importing tiles data (please only load at level 1)
        with open('data/tiles.json', encoding='utf-8') as data:
            self.tile_data=json.load(data)
        with open('gfx/colours/tiles.json', encoding='utf-8') as gfx:
            self.tile_gfx=json.load(gfx)
        # Test: Full of grass
        self.path_map.walkable[:]=True
        self.path_map.transparent[:]=True
        self.graphics_map=numpy.full((height, width), Tile('.', (106, 190, 48), (57, 60, 50)))
        self.destructible=numpy.full((height, width), True)
        self.explored=numpy.full((height, width), False)
        # Test: Dirt paths
        x_dest=self.cave_y(5, 0, self.height-6, 'ground_dirt', 50, 50, 1, 1, 3)
        x_dest=self.cave_y(5, 0, self.height-1, 'ground_dirt', 100, 100, 1, 0, 2)
        # Test: Dirt walls
        y_dest=self.cave_x(13, 0, self.width-35, 'wall_dirt', 15, 15, 1, 1, 2)

    def recompute_fov(self, x, y, radius, light_walls, algorithm):
        self.path_map.compute_fov(x, y, radius, light_walls, algorithm)
    
    # www.roguebasin.com/index.php?title=Basic_directional_dungeon_generation
    # Pretty useful, can be used for caves, beaten paths (straight paths would be pretty slow I tell ya), rivers, etc
    # tile: fills the entire path with it
    # roughness (0~100%): how often the path changes in width throughout the journey
    # wind (0~100%): how often the path changes in left border
    # swole: how big of a change the path can get
    # width_min: how smallest it could get

    def cave_y(self, x_origin, y_origin, y_dest, tile_name, roughness, wind, swole, width_min, width_max):
        # Load tile
        tile=Tile(self.tile_gfx[tile_name]['char'], tuple(self.tile_gfx[tile_name]['colour_lit']), tuple(self.tile_gfx[tile_name]['colour_dim']))
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
            # Implement per-tile transparent/walkable database/factory please, or actual grass classes or sth
            self.path_map.walkable[y, x_current:x_current+width_current]=self.tile_data[tile_name]['walkable']
            self.path_map.transparent[y, x_current:x_current+width_current]=self.tile_data[tile_name]['transparent']
            self.destructible[y, x_current:x_current+width_current]=self.tile_data[tile_name]['destructible']
            self.graphics_map[y, x_current:x_current+width_current]=tile
            # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
        # Returns x_current because it's the end of the road (level transitions/'stairs')
        return x_current

    def cave_x(self, y_origin, x_origin, x_dest, tile_name, roughness, wind, swole, height_min, height_max):
        # Load tile
        tile=Tile(self.tile_gfx[tile_name]['char'], tuple(self.tile_gfx[tile_name]['colour_lit']), tuple(self.tile_gfx[tile_name]['colour_dim']))
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
            # Implement per-tile transparent/walkable database/factory please, or actual grass classes or sth
            self.path_map.walkable[y_current:y_current+height_current, x]=self.tile_data[tile_name]['walkable']
            self.path_map.transparent[y_current:y_current+height_current, x]=self.tile_data[tile_name]['transparent']
            self.destructible[y_current:y_current+height_current, x]=self.tile_data[tile_name]['destructible']
            self.graphics_map[y_current:y_current+height_current, x]=tile
            # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
        # Returns x_current because it's the end of the road (level transitions/'stairs')
        return y_current

    