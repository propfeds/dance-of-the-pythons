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
                if game_map.path_map.fov[y, x]:
                    display.tiles[["ch", "fg"]][y, x]=ord(game_map.graphics_map[y, x].char), (*game_map.graphics_map[y, x].lit_colour, 255)
                    game_map.explored[y, x]=True
                elif game_map.explored[y, x]:
                    display.tiles[["ch", "fg"]][y, x]=ord(game_map.graphics_map[y, x].char), (*game_map.graphics_map[y, x].dim_colour, 255)
    render_ordered_entities=sorted(entities, key=lambda x: x.render_order.value)
    for entity in render_ordered_entities:
        if game_map.path_map.fov[entity.y, entity.x]:
            display.tiles[["ch", "fg"]][entity.y, entity.x]=ord(entity.char), (*entity.colour, 255)
    display.blit(root_console, 0, 0, 0, 0, terminal_width, terminal_height)

def clear_all(display, entities):
    for entity in entities:
        display.tiles[["ch"]][entity.y, entity.x]=ord(' ')