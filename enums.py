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

class Factions(Enum):
    NEUTRAL=0
    ALLY=1
    ENEMY=2

class RenderOrder(Enum):
    CORPSE=-1
    FURNITURE=0
    ITEM=1
    ACTOR_SHORT=2   # Mice
    ENVIRONMENT=3   # explosion smoke, particles
    ACTOR=4