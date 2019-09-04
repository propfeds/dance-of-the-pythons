import tcod
import tcod.event
import json
from map_objects.game_map import GameMap
from components.inventory import Inventory
from entity import Entity
from renderer import RenderOrder, render_all, erase_entities
from game_states import GameStates
from input_handler import handle_event
from spawner import Spawner, Factions


from components.ai import NeutralAggro
from map_objects.generator import generate_test_area

def main():
    # Importing data from config
    with open('data/config.json') as cfg:
        data=json.load(cfg)
    terminal_width=data['terminal_width']
    terminal_height=data['terminal_height']
    map_width=data['map_width']
    map_height=data['map_height']
    fov_algorithm=data['fov_algorithm']
    fov_light_walls=data['fov_light_walls']
    fov_radius=data['fov_radius']
    # Init root console
    tcod.console_set_custom_font('gfx/fonts/terminal16x16_gs_ro.png', tcod.FONT_TYPE_GREYSCALE | tcod.tcod.FONT_LAYOUT_CP437)
    console_root=tcod.console_init_root(terminal_width, terminal_height, 'Python Game Lol', False, tcod.RENDERER_SDL2, 'C', False)
    console_display=tcod.console.Console(terminal_width, terminal_height, 'C')
    with open('gfx/colours/palette.json') as colours:
        palette=json.load(colours)
    console_display.bg[:]=palette['terminal_green']
    #interface=tcod.console.Console(terminal_width, map_height, 'C')
    game_map=GameMap(map_width, map_height)
    spawner=Spawner(map_width, map_height, 0)
            # Testing creatures
    generate_test_area(game_map, spawner)
    player=spawner.entities[0]
    # Then generate map
    fov_recompute=True
    # message log
    game_state=GameStates.TURN_PLAYER
    prev_game_state=game_state
    #targeting_item=None
    # Rendering for the first time
    game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
    render_all(console_root, console_display, spawner.entities, game_map, fov_recompute)
    fov_recompute=False
    tcod.console_flush()
    # Game loop
    while True:
        # Render
        if fov_recompute:
            game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
        render_all(console_root, console_display, spawner.entities, game_map, fov_recompute)
        fov_recompute=False
        tcod.console_flush()
        erase_entities(console_display, spawner.entities, game_map)
        # Processing action
        action=handle_event(game_state)
        move=action.get('move')
        pickup=action.get('pickup')
        take_inventory=action.get('take_inventory')
        fullscreen=action.get('fullscreen')
        exit=action.get('exit')
        # Player's Turn
        results_player=[]
        # Results: Extend if player turn ends and append if doesn't?
        if game_state==GameStates.TURN_PLAYER:
            if move:
                dx, dy=move
                results_movement=player.handle_move(player, dx, dy, spawner, game_map, swappable=True)
                if results_movement:
                    results_player.extend(results_movement)
                    fov_recompute=True
                    game_state=GameStates.TURN_ALLY

            elif pickup: # Should implement a pickup list like POWDER
                for entity in spawner.entities:
                    if entity.item and entity.x==player.x and entity.y==player.y:
                        print('ADD ITEM')   # Add item
                        break
                else:
                    print('GRAB GROUND')    # Message log to grab ground
        
        if take_inventory:
            prev_game_state=game_state
            game_state=GameStates.MENU_INVENTORY
        
        if exit:
            if game_state.value>=10:  # Game states >= 10 are menus: inventory, quipment, etc.
                game_state=prev_game_state
            if game_state.value>=20:  # Game states >= 20 are targetings
                results_player.append({'targeting_cancelled': True})
            # else brings up main menu
        
        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

        # Player turn messages: handled by an announcer (translation friendly probably)

        # Faction turns (handled by an announcer also)
        if game_state==GameStates.TURN_ALLY:
            for entity in spawner.entities:
                if entity.faction==Factions.ALLY and entity!=player:
                    results_ally=entity.ai.take_turn(spawner, game_map.path_map)
            game_state=GameStates.TURN_ENEMY
        
        if game_state==GameStates.TURN_ENEMY:
            for entity in spawner.entities:
                if entity.faction==Factions.ENEMY:
                    results_enemy=entity.ai.take_turn()
            game_state=GameStates.TURN_NEUTRAL
        
        if game_state==GameStates.TURN_NEUTRAL:
            for entity in spawner.entities:
                if entity.faction==Factions.NEUTRAL:
                    if entity.ai:
                        resutls_neutral=entity.ai.take_turn()
            game_state=GameStates.TURN_PLAYER


if __name__=='__main__':
    main()