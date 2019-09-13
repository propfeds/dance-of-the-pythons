import tcod
import json
import systems

class World:
    def __init__(self):
        self.renderer=systems.renderer.Renderer()
        self.spawner=systems.spawner.Spawner(0)
        self.terrain_map=systems.terrain_map.TerrainMap(self.renderer.config['consoles']['width'][0], self.renderer.config['consoles']['height'][0], 0)