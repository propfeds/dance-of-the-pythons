import tcod

def main():
    terminal_height=50
    terminal_width=80

    tcod.console_set_custom_font('consolas_unicode_10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    

if __name__=='__main__':
    main()