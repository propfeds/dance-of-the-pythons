from snecs import new_entity
from components import *

def spawn_player(world, x, y):
    return new_entity((
        Faction(0),
        Health(7, 300),
        InputControlled(),
        Inventory(20),
        Name('Player', 'Propunos'),
        Position(x, y),
        Render('@', 'main_3', 4),
        Stamina(5, 6, 6)
        ),
        world=world
    )