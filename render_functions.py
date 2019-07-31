import tcod
from enum import Enum

class RenderOrder(Enum):
    CORPSE=0
    ITEM=1
    ENVIRONMENT=2   # Bushes / tall grass, explosion smoke, particles
    ACTOR=3

def render_all():
    print('doo be doo')