import tcod
import tcod.event
import json
from map_objects.game_map import GameMap
from components.inventory import Inventory
from entity import Entity
from render_functions import RenderOrder, render_all
from game_states import GameStates
from input_handler import handle_key

def main():
    # Importing data from data/config.json
    with open('data/config.json') as cfg:
        data=json.load(cfg)
    terminal_width=data['terminal_width']
    terminal_height=data['terminal_height']
    map_width=data['map_width']
    map_height=data['map_height']
    fov_algorithm=data['fov_algorithm']
    fov_light_walls=bool(data['fov_light_walls'])
    fov_radius=data['fov_radius']

    # Init console, player and stuff
    player=Entity(25, 25, '@', tcod.yellow, 'Ratiel Snailface the Enchanter', 5, 1, 0, RenderOrder.ACTOR, False, None, None, None, Inventory(26))
    entities=[player]

    tcod.console_set_custom_font('data/arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    root_console=tcod.console_init_root(terminal_width, terminal_height, 'Dance of the Pythons', False, tcod.RENDERER_SDL2, 'C', False)
    display=tcod.console.Console(terminal_width, terminal_height, 'C') 
    #interface=tcod.console.Console(terminal_width, map_height, 'C')
    game_map=GameMap(map_width, map_height)
    # Then generate map
    fov_recompute=True
    # message log
    game_state=GameStates.PLAYER_TURN
    prev_game_state=game_state
    targeting_item=None
    # Rendering for the first time
    game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
    render_all(root_console, display, entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state)
    fov_recompute=False
    tcod.console_flush()
    # Game loop
    while True:
        for event in tcod.event.wait():
            if event.type=='QUIT':
                raise SystemExit()
            elif event.type=='KEYDOWN':
                if fov_recompute:
                    game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
                render_all(root_console, display, entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state)
                fov_recompute=False
                tcod.console_flush()
                # Clear All?
                action=handle_key(event, game_state)
                move=action.get('move')
                pickup=action.get('pickup')
                take_inventory=action.get('take_inventory')
                cancel=action.get('cancel')
                

if __name__=='__main__':
    main()