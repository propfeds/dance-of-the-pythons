import tcod
import json
import systems

class World:
    def __init__(self):
        renderer=systems.renderer.Renderer()
        spawner=systems.spawner.Spawner()