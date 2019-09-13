import tcod
import json
from data.enums import RenderOrder
from components.position import Position
from components.graphics import Graphics

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
        
    def render_routine(self, terrain_map, fov):
        self.render_terrain(terrain_map, fov)
        self.blit_all()
    
    def render_terrain(self, terrain_map, fov):
        # gather fov (array) from bitwise orring entities with both Vision and Companion components
        for y in range(terrain_map.width):
            for x in range(terrain_map.height):
                if fov[y, x]:
                    self.consoles[0].tiles[['ch', 'fg']][y, x]=ord(terrain_map.grounds[y, x].char), (*terrain_map.grounds[y, x].colour_lit, 255)
                    self.consoles[1].tiles[['ch', 'fg']][y, x]=ord(terrain_map.walls[y, x].char), (*terrain_map.walls[y, x].colour_lit, 255)
                    terrain_map.explored[y, x]=True
                elif terrain_map.explored[y, x]:
                    self.consoles[0].tiles[['ch', 'fg']][y, x]=ord(terrain_map.grounds[y, x].char), (*terrain_map.grounds[y, x].colour_dim, 255)
                    self.consoles[1].tiles[['ch', 'fg']][y, x]=ord(terrain_map.walls[y, x].char), (*terrain_map.walls[y, x].colour_dim, 255)

    def render_entities(self, spawner, fov):
        for entity in spawner.entities:
            if entity.components[Position] and entity.components[Graphics]:
                y=entity.components[Position].y
                x=entity.components[Position].x
                if fov[y, x]:
                    self.consoles[RenderOrder[entity.components[Graphics].render_order].value].tiles[['ch', 'fg']][y, x]=ord(entity.components[Graphics].char), (*entity.components[Graphics].colour, 255)

    def blit_all(self):
        for i, console in enumerate(self.consoles):
            console.blit(self.console_root, self.config['consoles']['x'][i], self.config['consoles']['y'][i], 0, 0, self.config['consoles']['width'][i], self.config['consoles']['height'][i])

    def erase_entities(self, spawner, fov):
        # gather fov (array) from bitwise orring entities with both Vision and Companion components
        for entity in spawner.entities:
            if entity.components[Position] and entity.components[Graphics]:
                y=entity.components[Position].y
                x=entity.components[Position].x
                if fov[y, x]:
                    self.consoles[RenderOrder[entity.components[Graphics].render_order].value].tiles[['ch']][y, x]=''