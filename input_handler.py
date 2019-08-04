import tcod
import tcod.event
from game_states import GameStates

def handle_event(game_state):
    for event in tcod.event.get():
        if event.type=='QUIT':
            raise SystemExit()
        elif event.type=='KEYDOWN':
            return handle_key(event, game_state)
    return {}

def handle_key(event, game_state):
    if event.scancode==tcod.KEY_ENTER and event.mod==tcod.event.KMOD_ALT:
        return {'fullscreen': True}
    # Global exit: Cancels targeting, exits menus and pulls up menu while playing
    if event.scancode==tcod.KEY_ESCAPE:
        return {'exit': True}
    if game_state==GameStates.TURN_PLAYER:
        return handle_player_key(event)
    return {}

def handle_player_key(event):
    # Movement
    if event.scancode==96 or event.sym=='k':
        return {'move': (0, -1)}
    elif event.scancode==90 or event.sym=='j':
        return {'move': (0, 1)}
    elif event.scancode==92 or event.sym=='h':
        return {'move': (-1, 0)}
    elif event.scancode==94 or event.sym=='l':
        return {'move': (1, 0)}
    elif event.scancode==95 or event.sym=='y':
        return {'move': (-1, -1)}
    elif event.scancode==97 or event.sym=='u':
        return {'move': (1, -1)}
    elif event.scancode==89 or event.sym=='b':
        return {'move': (-1, 1)}
    elif event.scancode==91 or event.sym=='n':
        return {'move': (1, 1)}
    elif event.scancode==93 or event.sym=='s':
        return {'move': (0, 0)}
    # Crab Grab
    if event.sym=='g':
        return {'pickup': True}
    # Unto the Big Bag
    if event.sym=='i':
        return {'take_inventory': True}
    return {}