import tcod
import json

class Renderer:
    def __init__(self):
        config=json.load(open('data/config.json'))
        tcod.console_set_custom_font('gfx/fonts/terminal12x16_gs_ro.png', tcod.FONT_TYPE_GREYSCALE | tcod.tcod.FONT_LAYOUT_CP437)
        console_root=tcod.console_init_root(config['terminal_width'], config['terminal_height'], 'Python Game Lol', False, tcod.RENDERER_SDL2, 'C', False)
        # consoles as array to blit by order
        consoles=[]
        # Map console
        consoles.append(config['consoles'][0]['width'], config['consoles'][0]['height'], 'C')
        # Then an UI background, then UI text display, then more UI popups