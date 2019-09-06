from map_objects.rectangle import Rectangle
from enums import Factions

def generate_test_area(game_map, spawner):
    game_map.fill_rect(Rectangle(0, 0, game_map.width, game_map.height), 'ground_grass')
    x_dest=game_map.cave_y(5, 0, game_map.height-6, 'ground_dirt', 35, 50, 1, 1, 3)
    x_dest=game_map.cave_y(5, 0, game_map.height-1, 'ground_dirt', 100, 100, 1, 0, 2)
    x_dest=game_map.cave_y(21, 0, game_map.height-7, 'wall_tree', 78, 78, 1, 3, 5)
    x_dest=game_map.cave_x(24, 0, game_map.width-1, 'wall_tree', 15, 15, 1, 3, 5)
    game_map.fill_rect(Rectangle(3, game_map.height-8, 7, game_map.height-4), 'wall_tent')
    game_map.fill_rect(Rectangle(3, game_map.height-6, 3, game_map.height-6), 'wall_tent_window')
    game_map.fill_rect(Rectangle(5, game_map.height-8, 5, game_map.height-8), 'ground_dirt')
    game_map.fill_rect(Rectangle(4, game_map.height-7, 6, game_map.height-5), 'ground_grass')
    y_dest=game_map.cave_x(13, 0, game_map.width-30, 'wall_dirt', 15, 15, 1, 1, 2)
    spawner.spawn_actor(0, 0, 'player', Factions.ALLY, game_map.path_map)
    spawner.spawn_actor(2, 2, 'snek_test', Factions.ALLY, game_map.path_map)
    spawner.spawn_actor(2, 0, 'focker_test', Factions.ENEMY, game_map.path_map)