from enum import Enum

class GameStates(Enum):
    DEATH=0         # Faction Departed
    PLAYER_TURN=1   # Faction Good
    ALLY_TURN=2     # Faction Good (your kin and charmed animals)
    ENEMY_TURN=3    # Faction Bad (humans)
    NEUTRAL_TURN=4  # Faction Neutral (traps, critters)

    MENU=10         # Supposed to be options?
    INVENTORY=11    # Press inventory then press key to pull up the item menu with options such as [drop, wield, use]
    TARGETING=12    # The cursed thing, but now with keyboard controls instead