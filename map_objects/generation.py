import tcod
from map_objects.tile import Tile
# Pretty useful, can be used for caves, beaten paths (straight paths would be pretty slow I tell ya), rivers, etc
# tile: fills the entire path with it
# roughness (0~100): how much the path changes in width throughout the journey
# wind (0~100): curveyness
# PASTED from http://www.roguebasin.com/index.php?title=Basic_directional_dungeon_generation
# This is the entrance and init part of the algorithm. The following is the iterative part, which repeats until the map is compliant with your requests (in this case, only length).

# Increment y by 1. This moves us up a line, so we're working on the one above the starting one on the first step. Check if a random number out of 100 is smaller than or equal to roughness. If it is, roll a random number between -2 and 2 (excluding 0). Add this number to the current width. If width is now smaller than 3, set it to 3. If larger than the map width, set it to the map width. Check if a random number out of 100 is smaller than or equal to windyness. If it is, roll a random number between -2 and 2 (excluding 0). Add this number to the current x. If x is now smaller than 0, set it to 0. If larger than the map width-3, set it to the map width-3. Place a rectangle from current x, current y, to current x + width, current y.

# This is where you can add any by-row events you need for the generator (a chance of a secret exit appearing on a left-most or right-most wall, or adding pillars in the middle of the cave). Add a small room or rectangle at the end.

# One thing you can add is a complexity number. Thus, for a complexity number of 1, the entire algorithm is run once. For 2, it's run twice on the same map. Thus, you occasionally get 2 paths that intersect, walk along each other (or on top of each other), diverge, and connect in interesting fashions. For 3 it's run thrice. Higher numbers generally have a cave complex enough that the directional element matters little. Another addition is running it sequentially like for complex maps, only with different directional elements. Run it once top-down, once left-right, and you have a cave that has no consistent direction to it, but at least some available for the player to choose from.

def generate_path_y(origin_x, origin_y, destination_y, tile, roughness, wind, game_map):
    print ('fuckoff')