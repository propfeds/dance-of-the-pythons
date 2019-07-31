import tcod
from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
            self.width=width
            self.height=height
            self.tiles=self.init_tiles()
    def init_tiles(self):
        # It should be iterating C order?
        tiles=[[Tile('.', tcod.white, 'White grass', True, True) for x in range(self.width)] for y in range(self.height)]
        return tiles