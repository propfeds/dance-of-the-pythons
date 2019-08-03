import tcod
from map_objects.tile import Tile
from random import randint

def cave_y(x_origin, y_origin, y_dest, tile_name, roughness, wind, swole, width_min, width_max, game_map):
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
                x_current=min(x_current, game_map.width-width_min)
        # Implement per-tile transparent/walkable database/factory please, or actual grass classes or sth
        # Generates dirt path
        game_map.path_map.walkable[y, x_current:x_current+width_current]=True
        game_map.path_map.transparent[y, x_current:x_current+width_current]=True
        game_map.graphics_map[y, x_current:x_current+width_current]=tile
        # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
    # Returns x_current because it's the end of the road (level transitions/'stairs')
    return x_current

# www.roguebasin.com/index.php?title=Basic_directional_dungeon_generation
# Pretty useful, can be used for caves, beaten paths (straight paths would be pretty slow I tell ya), rivers, etc
# tile: fills the entire path with it
# roughness (0~100%): how often the path changes in width throughout the journey
# wind (0~100%): how often the path changes in left border
# swole: how big of a change the path can get
# width_min: how smallest it could get