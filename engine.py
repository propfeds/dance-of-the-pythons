import tcod
import tcod.event
import json
from map_objects.game_map import GameMap
from components.inventory import Inventory
from entity import Entity
from render_functions import RenderOrder, render_all, clear_all
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

    # Init root console and player
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
                # Render
                if fov_recompute:
                    game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
                render_all(root_console, display, entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state)
                fov_recompute=False
                tcod.console_flush()
                clear_all(display, entities)
                # Processing action
                action=handle_key(event, game_state)
                move=action.get('move')
                pickup=action.get('pickup')
                take_inventory=action.get('take_inventory')
                fullscreen=action.get('fullscreen')
                exit=action.get('exit')

                player_turn_results=[]
                if game_state==GameStates.PLAYER_TURN:
                    if move:
                        dx, dy=move
                        if game_map.path_map.walkable[player.y+dy, player.x+dx]:
                            # target=get_blocking_entities(entities, player.x+dx, player.y+dy)
                            if False:
                                print('PLACEHOLDER')
                            # if target:
                                # depends on object: if enemy attack, if ally swap, if vendor/chest interact
                            else:
                                player.move(dx, dy)
                                fov_recompute=True
                            game_state=GameStates.ALLY_TURN
                    elif pickup: # Should implement a pickup list like POWDER
                        for entity in entities:
                            if entity.item and entity.x==player.x and entity.y==player.y:
                                print('ADD ITEM')   # Add item
                                break
                        else:
                            print('GRAB GROUND')    # Message log to grab ground
                
                if take_inventory:
                    prev_game_state=game_state
                    game_state=GameStates.INVENTORY
                
                if exit:
                    if game_state>=10:  # Game states >= 10 are menus: inventory, targeting, etc.
                        game_state=prev_game_state
                    if game_state>=20:  # Game states >= 20 are targetings
                        player_turn_results.append({'targeting_cancelled': True})
                    # else brings up main menu
                
                if fullscreen:
                    tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

                # Player turn messages

                # Faction turns (includes message logs built within)
                if game_state==GameStates.ALLY_TURN:
                        game_state=GameStates.ENEMY_TURN
                
                if game_state==GameStates.ENEMY_TURN:
                        game_state=GameStates.NEUTRAL_TURN
                
                if game_state==GameStates.NEUTRAL_TURN:
                        game_state=GameStates.PLAYER_TURN
                
                break


if __name__=='__main__':
    main()