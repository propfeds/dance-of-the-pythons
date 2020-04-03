# Constants, enums and shtuff related only to current game mode

interface={
    'window'={
        'w'=64,
        'h'=36,
    },
    'log'={
        'x'=1,
        'y'=28,
        'w'=47,
        'h'=8,
    },
    'char'={
        'x'=49,
        'y'=28,
        'w'=15,
        'h'=8,
    },
    # Multi-purpose area: menu, inspect, inventory, target listing
    'menu'={
        'x'=49,
        'y'=1,
        'w'=15,
        'h'=26,
    },
    'overlay'='''
                                                ┌─Menu name─────
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
                                                │
┌─Combat Log────────────────────────────────────X─Insert name───
│                                               │
│                                               │
│                                               │
│                                               │
│                                               │
│                                               │
│                                               │
│                                               │'''
}

gameplay={
    'window_title'='Project Regular 2 III: Dance of the Rewrites',
}

# Not actually enums

# Nature is aggressive neutral, tame neutral has no faction
factions={
    'local': 0,
    'local_scum': 1,
    'human': 2,
    'nature': 3,
}

# Particles can be smoke (actually conceals entity char), spell effects etc.
render_order={
    'ground': 0,
    'wall': 1,
    'item': 2,
    'actor_short': 3,
    'actor': 4,
    'particle': 5,
}