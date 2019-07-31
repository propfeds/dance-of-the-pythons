import tcod
from enum import Enum

class RenderOrder(Enum):
    TILE=0
    CORPSE=1
    ITEM=2
    ACTOR=3