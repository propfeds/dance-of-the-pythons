import tcod
import json

class Renderer:
    def __init__(self):
        self.config=json.load(open('data/config.json'))
        self.palette=json.load(open('data/palette.json'))
        tcod.console_set_custom_font('data/fonts/terminal12x16_gs_ro.png', tcod.FONT_TYPE_GREYSCALE | tcod.tcod.FONT_LAYOUT_CP437)
        self.console_root=tcod.console_init_root(self.config['terminal_width'], self.config['terminal_height'], 'Python Game Lol', False, tcod.RENDERER_SDL2, 'C', False)
        # consoles as array to blit by order
        self.consoles=[]
        # Grounds, walls, entities and particles consoles (index 0~6)
        # Then an UI background, then UI text display, then more UI popups (7~9)
        for i in range(10):
            self.consoles.append(tcod.console.Console(self.config['consoles']['width'][i], self.config['consoles']['height'][i], 'C'))
        
    def render_routine(self):
        self.megablit()
        pass

    def megablit(self):
        for i, console in enumerate(self.consoles):
            console.blit(self.console_root, self.config['consoles']['x'][i], self.config['consoles']['y'][i], 0, 0, self.config['consoles']['width'][i], self.config['consoles']['height'][i])