import tcod
from enum import Enum

class RenderOrder(Enum):
    CORPSE=0
    ITEM=1
    ENVIRONMENT=2   # Bushes / tall grass, explosion smoke, particles
    ACTOR=3

def render_all(display, entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state):
    # [y, x] arrays remember
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible=game_map.path_map.fov[y, x]
                if visible:
                    display.print(x, y, game_map.graphics_map[y][x].char, game_map.graphics_map[y][x].lit_colour)
                    game_map.graphics_map[y][x].explored=True
                elif game_map.graphics_map[y][x].explored:
                    display.print(x, y, game_map.graphics_map[y][x].char, game_map.graphics_map[y][x].dim_colour)
    render_ordered_entities=sorted(entities, key=lambda x:x.render_order.value)
    for entity in render_ordered_entities:
        if game_map.path_map.fov[y, x]:
            display.print(x, y, entity.char, entity.colour)
    # 1st arg: console 0 == root
    display.blit(0, 0, 0, 0, 0, terminal_width, terminal_height)