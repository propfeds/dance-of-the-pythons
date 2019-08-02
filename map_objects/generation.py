import tcod
from map_objects.tile import Tile
from random import randint

def generate_path_y(origin_x, origin_y, dest_y, tile, roughness, wind, swole, min_width, game_map):
    # step determines whether the algo runs up or down
    step=1
    if(origin_y>dest_y):
        step=-1
    current_width=min_width
    current_x=origin_x
    for y in range(origin_y, dest_y+step, step):
        rough_roll=randint(0, 100)
        if rough_roll<roughness:
            current_width=max(min_width, current_width+randint(-swole, swole))
        if y!=origin_y:
            wind_roll=randint(0, 100)
            if wind_roll<wind:
                current_x=max(0, current_x+randint(-swole, swole))
                current_x=min(current_x, game_map.width-min_width)
        # Implement per-tile transparent/pathable database/factory please, or actual grass classes or sth
        # Generates dirt path
        game_map.path_map.walkable[y, current_x:current_x+current_width]=True
        game_map.path_map.transparent[y, current_x:current_x+current_width]=True
        game_map.graphics_map[y, current_x:current_x+current_width]=Tile('.', (138, 111, 48), (82, 75, 36))
        # This is where I could add events (a chance of a tent appearing on a branch from the path, or some fixture like torches).
    # Returns current_x because it's the end of the road (level transitions/'stairs')
    return current_x

# www.roguebasin.com/index.php?title=Basic_directional_dungeon_generation
# Pretty useful, can be used for caves, beaten paths (straight paths would be pretty slow I tell ya), rivers, etc
# tile: fills the entire path with it
# roughness (0~100%): how often the path changes in width throughout the journey
# wind (0~100%): how often the path changes in left border
# swole: how big of a change the path can get
# min_width: how smallest it could get