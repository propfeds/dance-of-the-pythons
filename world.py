import tcod
import systems
from json import load

class World:
    def __init__(self):
        self.renderer=systems.renderer.Renderer()
        self.spawner=systems.spawner.Spawner(0)
        self.terrain_map=systems.terrain_map.TerrainMap(
            self.renderer.config['consoles']['map']['w'][0],
            self.renderer.config['consoles']['map']['h'][0], 0)