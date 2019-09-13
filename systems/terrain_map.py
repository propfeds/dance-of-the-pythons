import tcod
import tcod.map
import numpy
import json
from random import randint
from systems.map.tile import Tile
from systems.geometry import Rectangle

class TerrainMap:
    def __init__(self, width, height, level):
        self.width=width
        self.height=height
        self.level=level
        self.path_map=tcod.map.Map(width, height, 'C')
        self.grounds=numpy.full((height, width), None)
        self.walls=numpy.full((height, width), None)
        self.explored=numpy.full((height, width), False)
        # Importing tiles data (please only load at level 1)
        self.palette=json.load(open('gfx/palette.json'))
        self.ground_data=json.load(open('data/grounds.json', encoding='utf-8'))
        self.wall_data=json.load(open('gfx/tiles.json', encoding='utf-8'))
        
    def fill_rect(self, rect, is_wall, tile_name):
        # is_wall: if the tiles filled are gonna be walls
        if is_wall:
            self.walls[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=Tile(self.wall_data[tile_name]['graphics']['char'], tuple(self.palette[self.wall_data[tile_name]['graphics']['colour_lit']]), tuple(self.palette[self.wall_data[tile_name]['graphics']['colour_lit']]))
            self.path_map.walkable[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.wall_data[tile_name]['properties']['walkable']
            self.path_map.transparent[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.wall_data[tile_name]['properties']['transparent']
        else:
            self.grounds[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=Tile(self.ground_data[tile_name]['graphics']['char'], tuple(self.palette[self.ground_data[tile_name]['graphics']['colour_lit']]), tuple(self.palette[self.ground_data[tile_name]['graphics']['colour_lit']]))
            self.path_map.walkable[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.ground_data[tile_name]['properties']['walkable']
            self.path_map.transparent[rect.y1:rect.y2+1, rect.x1:rect.x2+1]=self.ground_data[tile_name]['properties']['transparent']
    
    # www.roguebasin.com/index.php?title=Basic_directional_dungeon_generation
    # Pretty useful, can be used for caves, beaten paths (straight paths would be pretty slow I tell ya), rivers, etc
    # tile_name: fills the entire path with it
    # roughness (0~100%): how often the path changes in width throughout the journey
    # wind (0~100%): how often the path changes in left border
    # swole: how big of a change the path can get
    # width_min/max: how small/big it could get

    def cave_y(self, x_origin, y_origin, y_dest, is_wall, tile_name, roughness, wind, swole, width_min, width_max):
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
            if is_wall:
                self.fill_rect(Rectangle(x_current, y, x_current+width_current-1, y), True, tile_name)
            else:
                self.fill_rect(Rectangle(x_current, y, x_current+width_current-1, y), False, tile_name)
            # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
        # Returns x_current because it's the end of the road (level transitions/'stairs')
        return x_current

    def cave_x(self, y_origin, x_origin, x_dest, is_wall, tile_name, roughness, wind, swole, height_min, height_max):
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
            if is_wall:
                self.fill_rect(Rectangle(x, y_current, x, y_current+height_current-1), True, tile_name)
            else:
                self.fill_rect(Rectangle(x, y_current, x, y_current+height_current-1), False, tile_name)
            # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
        # Returns x_current because it's the end of the road (level transitions/'stairs')
        return y_current