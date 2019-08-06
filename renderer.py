import tcod
from enum import Enum

class RenderOrder(Enum):
    CORPSE=-1
    FURNITURE=0
    ITEM=1
    ACTOR_SHORT=2   # Mice
    ENVIRONMENT=3   # explosion smoke, particles
    ACTOR=4

def render_all(console_root, console_display, entities, game_map, fov_recompute):
    # [y, x] arrays remember
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                if game_map.path_map.fov[y, x]:
                    console_display.tiles[["ch", "fg"]][y, x]=ord(game_map.graphics[y, x].char), (*game_map.graphics[y, x].colour_lit, 255)
                    game_map.explored[y, x]=True
                elif game_map.explored[y, x]:
                    console_display.tiles[["ch", "fg"]][y, x]=ord(game_map.graphics[y, x].char), (*game_map.graphics[y, x].colour_dim, 255)
    render_ordered_entities=sorted(entities, key=lambda x: x.render_order.value)
    for entity in render_ordered_entities:
        if game_map.path_map.fov[entity.y, entity.x]:
            console_display.tiles[["ch", "fg"]][entity.y, entity.x]=ord(entity.char), (*entity.colour, 255)
    console_display.blit(console_root, 0, 0, 0, 0, game_map.width, game_map.height)

def erase_entities(console_display, entities, game_map):
    for entity in entities:
        if game_map.path_map.fov[entity.y, entity.x]:
            console_display.tiles[["ch", "fg"]][entity.y, entity.x]=ord(game_map.graphics[entity.y, entity.x].char), (*game_map.graphics[entity.y, entity.x].colour_lit, 255)

#def erase_entity(display, entity):
 #   display.tiles[["ch"]][entity.y, entity.x]=ord(' ')