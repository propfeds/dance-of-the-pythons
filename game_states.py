from enum import Enum

class GameStates(Enum):
    DEATH=0
    PLAYER_TURN=1   # Faction Good
    ALLY_TURN=2     # Faction Good (your fellow snekmen and charmed sneks)
    ENEMY_TURN=3    # Faction Bad (humans)
    NEUTRAL_TURN=4  # Faction Neutral (traps, critters, some human NPCs, aggressiveness depends on AI type)

    MENU=10         # Supposed to be options?
    INVENTORY=11    # Press inventory then press key to pull up the item menu with options such as [drop, wield, use]
    TARGETING=12    # The cursed thing, but now with keyboard controls instead