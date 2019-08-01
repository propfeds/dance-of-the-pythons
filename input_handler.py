import tcod
from game_states import GameStates

def handle_key(event, game_state):
    if event.scancode==tcod.KEY_ENTER and event.mod==tcod.event.KMOD_ALT:
        return {'fullscreen': True}
    # Global exit: Cancels targeting, exits menus and pulls up menu while playing
    if event.scancode==tcod.KEY_ESCAPE:
        return {'exit': True}
    if game_state==GameStates.PLAYER_TURN:
        return handle_player_key(event)
    return {}

def handle_player_key(event):
    # Movement
    if event.scancode==tcod.KEY_KP8 or event.sym=='k':
        return {'move': (0, -1)}
    elif event.scancode==tcod.KEY_KP2 or event.sym=='j':
        return {'move': (0, 1)}
    elif event.scancode==tcod.KEY_KP4 or event.sym=='h':
        return {'move': (-1, 0)}
    elif event.scancode==tcod.KEY_KP6 or event.sym=='l':
        return {'move': (1, 0)}
    elif event.scancode==tcod.KEY_KP7 or event.sym=='y':
        return {'move': (-1, -1)}
    elif event.scancode==tcod.KEY_KP9 or event.sym=='u':
        return {'move': (1, -1)}
    elif event.scancode==tcod.KEY_KP1 or event.sym=='b':
        return {'move': (-1, 1)}
    elif event.scancode==tcod.KEY_KP3 or event.sym=='n':
        return {'move': (1, 1)}
    # Crab Grab
    if event.sym=='g':
        return {'pickup': True}
    # Unto the Big Bag
    if event.sym=='i':
        return {'take_inventory': True}
    return {}