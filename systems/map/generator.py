from systems.geometry import Rectangle
from data.enums import Factions

def generate_test_area(terrain_map, spawner):
    terrain_map.fill_rect(Rectangle(0, 0, terrain_map.width, terrain_map.height), False, 'grass')
    x_dest=terrain_map.cave_y(5, 0, terrain_map.height-6, False, 'dirt', 35, 50, 1, 1, 3)
    x_dest=terrain_map.cave_y(5, 0, terrain_map.height-1, False, 'dirt', 100, 100, 1, 0, 2)
    x_dest=terrain_map.cave_y(21, 0, terrain_map.height-7, True, 'tree', 78, 78, 1, 3, 5)
    x_dest=terrain_map.cave_x(24, 0, terrain_map.width-1, True, 'tree', 15, 15, 1, 3, 5)
    terrain_map.fill_rect(Rectangle(3, terrain_map.height-8, 7, terrain_map.height-4), True, 'tent')
    terrain_map.fill_rect(Rectangle(3, terrain_map.height-6, 3, terrain_map.height-6), True, 'tent_window')
    terrain_map.fill_rect(Rectangle(5, terrain_map.height-8, 5, terrain_map.height-8), False, 'dirt')
    terrain_map.fill_rect(Rectangle(4, terrain_map.height-7, 6, terrain_map.height-5), False, 'grass')
    terrain_map.fill_rect(Rectangle(0, 0, 3, 3), True, 'grass')
    y_dest=terrain_map.cave_x(13, 0, terrain_map.width-45, True, 'dirt', 15, 15, 1, 1, 2)
    spawner.spawn_actor(0, 0, 'player', Factions.ALLY, terrain_map.path_map)
    spawner.spawn_actor(2, 2, 'snek_test', Factions.ALLY, terrain_map.path_map)
    spawner.spawn_actor(2, 0, 'focker_test', Factions.ENEMY, terrain_map.path_map)