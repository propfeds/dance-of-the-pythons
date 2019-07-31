import tcod
import tcod.event
import json

def main():
    # Importing data from config.json
    with open('config.json') as cfg:
        data=json.load(cfg)
    terminal_width=data['terminal_width']
    terminal_height=data['terminal_height']
    map_width=data['map_width']
    map_height=data['map_height']
    max_monsters_per_room=data['max_monsters_per_room']
    max_items_per_room=data['max_items_per_room']
    fov_algorithm=data['fov_algorithm']
    fov_light_walls=bool(data['fov_light_walls'])
    fov_radius=data['fov_radius']

    # Init console
    tcod.console_set_custom_font('consolas_unicode_10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(terminal_width, terminal_height, 'Dance of the Pythons', False, tcod.RENDERER_SDL2, 'F', False)
    while True:
        for event in tcod.event.wait():
            if event.type=='QUIT':
                raise SystemExit()
            elif event.type=='KEYDOWN':
                print(event)

if __name__=='__main__':
    main()