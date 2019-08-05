import tcod
import tcod.event
import json
from map_objects.game_map import GameMap
from components.inventory import Inventory
from entity import Entity
from renderer import RenderOrder, render_all, erase_all, erase_entity
from game_states import GameStates
from input_handler import handle_event
from spawner import Spawner, Factions
from ai import NeutralAggro

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
    root_console=tcod.console_init_root(terminal_width, terminal_height, 'Python: Yuwanda\'s Awakening', False, tcod.RENDERER_SDL2, 'C', False)
    display=tcod.console.Console(terminal_width, terminal_height, 'C')
    with open('gfx/colours/palette.json') as colours:
        palette=json.load(colours)
    display.bg[:]=palette['terminal_green']
    #interface=tcod.console.Console(terminal_width, map_height, 'C')
    game_map=GameMap(map_width, map_height)
    spawner=Spawner(map_width, map_height, 0, game_map.path_map)
    spawner.spawn_actor(0, 0, 'player', Factions.ALLY)
    player=spawner.entities[0]
            # Testing creatures
    spawner.spawn_actor(2, 2, 'snek_test', Factions.ALLY)
    spawner.spawn_actor(2, 0, 'focker_test', Factions.ALLY)
    # Then generate map
    fov_recompute=True
    # message log
    game_state=GameStates.TURN_PLAYER
    prev_game_state=game_state
    #targeting_item=None
    # Rendering for the first time
    game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
    render_all(root_console, display, spawner.entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state)
    fov_recompute=False
    tcod.console_flush()
    # Game loop
    while True:
        # Render
        if fov_recompute:
            game_map.recompute_fov(player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
        render_all(root_console, display, spawner.entities, player, game_map, fov_recompute, terminal_width, terminal_height, game_state)
        fov_recompute=False
        tcod.console_flush()
        erase_all(display, spawner.entities)
        # Processing action
        action=handle_event(game_state)
        move=action.get('move')
        pickup=action.get('pickup')
        take_inventory=action.get('take_inventory')
        fullscreen=action.get('fullscreen')
        exit=action.get('exit')
        # Player's Turn
        player_results=[]
        # Results: Extend if player turn ends and append if doesn't?
        if game_state==GameStates.TURN_PLAYER:
            if move:
                dx, dy=move
                if dx==0 and dy==0:
                    player_results.extend({'wait': True})
                    print('I\'m still waiting')
                    game_state=GameStates.TURN_ALLY
                else:
                    response=spawner.check_collision(player.x+dx, player.y+dy)
                    target=response.get('collide')
                    if target:
                        # Depends on object: if enemy attack, if ally swap (sneks not gonna brek cuz they pathable)
                        if target.faction==Factions.ENEMY or target.ai==NeutralAggro():
                            print('A')  # reemmber to extend results
                            game_state=GameStates.TURN_ALLY
                        else:
                            if (not target.walkable) and (not player.walkable): # Non sneks (cheesy circumvention) and if player is in mouse form or sth they'll phase into the enemy
                                player_results.extend(player.swap(target))
                            else:
                                player.move(dx, dy, spawner.block_map)
                            game_state=GameStates.TURN_ALLY
                    elif (not response.get('blocked')) and (not response.get('outofbounds')):
                        player.move(dx, dy, spawner.block_map)
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
                player_results.append({'targeting_cancelled': True})
            # else brings up main menu
        
        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

        # Player turn messages: handled by an announcer (translation friendly probably)

        # Faction turns (handled by an announcer also)
        if game_state==GameStates.TURN_ALLY:
                game_state=GameStates.TURN_ENEMY
        
        if game_state==GameStates.TURN_ENEMY:
                game_state=GameStates.TURN_NEUTRAL
        
        if game_state==GameStates.TURN_NEUTRAL:
                game_state=GameStates.TURN_PLAYER


if __name__=='__main__':
    main()