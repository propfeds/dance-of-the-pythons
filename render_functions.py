import tcod
from enum import Enum

class RenderOrder(Enum):
    CORPSE=0
    ITEM=1
    ENVIRONMENT=2   # Bushes / tall grass, explosion smoke, particles
    ACTOR=3

def render_all(root_console, display, entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state):
    # [y, x] arrays remember
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible=game_map.path_map.fov[y, x]
                if visible:
                    display.tiles[y, x]=(ord(game_map.graphics_map[y][x].char), (*game_map.graphics_map[y][x].colour_lit, 255), (*tcod.black, 255))
                    game_map.graphics_map[y][x].explored=True
                elif game_map.graphics_map[y][x].explored:
                    display.tiles[y, x]=(ord(game_map.graphics_map[y][x].char), (*game_map.graphics_map[y][x].colour_dim, 255), (*tcod.black, 255))
    render_ordered_entities=sorted(entities, key=lambda x:x.render_order.value)
    for entity in render_ordered_entities:
        if game_map.path_map.fov[entity.y, entity.x]:
            display.print(entity.x, entity.y, entity.char, entity.colour)
    # 1st arg: console 0 == root
    display.blit(root_console, 0, 0, 0, 0, terminal_width, terminal_height)

def clear_all(display, entities):
    for entity in entities:
        display.tiles[entity.y, entity.x]=(ord(' '), (*tcod.black, 255), (*tcod.black, 255))