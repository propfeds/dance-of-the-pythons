import tcod
from game_states import GameStates

def handle(event, game_state):
    if event.scancode==tcod.KEY_ENTER and event.mod==tcod.event.KMOD_ALT:
        return {'fullscreen': True}
    return {}
