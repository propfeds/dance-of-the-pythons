from systems.geometry import Rectangle
from data.enums import Factions

def generate_test_area(game_map, spawner):
    game_map.fill_rect(Rectangle(0, 0, game_map.width, game_map.height), False, 'grass')
    x_dest=game_map.cave_y(5, 0, game_map.height-6, False, 'dirt', 35, 50, 1, 1, 3)
    x_dest=game_map.cave_y(5, 0, game_map.height-1, False, 'dirt', 100, 100, 1, 0, 2)
    x_dest=game_map.cave_y(21, 0, game_map.height-7, True, 'tree', 78, 78, 1, 3, 5)
    x_dest=game_map.cave_x(24, 0, game_map.width-1, True, 'tree', 15, 15, 1, 3, 5)
    game_map.fill_rect(Rectangle(3, game_map.height-8, 7, game_map.height-4), True, 'tent')
    game_map.fill_rect(Rectangle(3, game_map.height-6, 3, game_map.height-6), True, 'tent_window')
    game_map.fill_rect(Rectangle(5, game_map.height-8, 5, game_map.height-8), False, 'dirt')
    game_map.fill_rect(Rectangle(4, game_map.height-7, 6, game_map.height-5), False, 'grass')
    game_map.fill_rect(Rectangle(0, 0, 3, 3), True, 'grass')
    y_dest=game_map.cave_x(13, 0, game_map.width-45, True, 'dirt', 15, 15, 1, 1, 2)
    spawner.spawn_actor(0, 0, 'player', Factions.ALLY, game_map.path_map)
    spawner.spawn_actor(2, 2, 'snek_test', Factions.ALLY, game_map.path_map)
    spawner.spawn_actor(2, 0, 'focker_test', Factions.ENEMY, game_map.path_map)