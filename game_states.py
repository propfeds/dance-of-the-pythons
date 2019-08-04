from enum import Enum

class GameStates(Enum):
    TURN_PLAYER=0   # Team Good
    TURN_ALLY=1     # Team Good (your kin and charmed animals)
    TURN_ENEMY=2    # Team Bad (humans)
    TURN_NEUTRAL=3  # Team Neutral (traps, critters)
    DEATH=4         # Welcome to the Hollows

    MENU_PAUSE=10             # Supposed to be options in the middle of the game
    MENU_INVENTORY=11        # Press inventory then press key to pull up the item menu with options such as [drop, wield, use]
    MENU_EQUIP=12        # You know where you wear that shiny plate mail

    MENU_TARGET_POINT=20  # The cursed thing, but now with keyboard controls instead
    MENU_TARGET_DIR=21    # Nine directions which if self-target (NumPad5 or s) fires to ground