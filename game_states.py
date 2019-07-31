from enum import Enum

class GameStates(Enum):
    DEATH=0         # Welcome to the Hollows
    PLAYER_TURN=1   # Team Good
    ALLY_TURN=2     # Team Good (your kin and charmed animals)
    ENEMY_TURN=3    # Team Bad (humans)
    NEUTRAL_TURN=4  # Team Neutral (traps, critters)

    MENU=10             # Supposed to be options?
    INVENTORY=11        # Press inventory then press key to pull up the item menu with options such as [drop, wield, use]
    EQUIPMENT=12        # You know where you wear that shiny plate mail
    POINT_TARGETING=13  # The cursed thing, but now with keyboard controls instead
    DIR_TARGETING=14    # Nine directions which if self-target (NumPad5 or s) fires to ground