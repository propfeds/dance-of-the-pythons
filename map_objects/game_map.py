import tcod
from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
            self.width=width
            self.height=height
            self.tiles=self.init_tiles()
    def init_tiles(self):
        # True: walls!
        tiles=[[Tile('#', tcod.grey, 'Grey brick wall', False, False) for y in range(self.height)] for x in range(self.width)]
        return tiles