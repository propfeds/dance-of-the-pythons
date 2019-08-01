from enum import Enum

class GameStates(Enum):
    PLAYER_TURN=0   # Team Good
    ALLY_TURN=1     # Team Good (your kin and charmed animals)
    ENEMY_TURN=2    # Team Bad (humans)
    NEUTRAL_TURN=3  # Team Neutral (traps, critters)
    DEATH=4         # Welcome to the Hollows

    MENU=10             # Supposed to be options?
    INVENTORY=11        # Press inventory then press key to pull up the item menu with options such as [drop, wield, use]
    EQUIPMENT=12        # You know where you wear that shiny plate mail

    POINT_TARGETING=20  # The cursed thing, but now with keyboard controls instead
    DIR_TARGETING=21    # Nine directions which if self-target (NumPad5 or s) fires to ground