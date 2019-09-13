from enum import Enum

class GameStates(Enum):
    DEATH=-1
    GAME=0
    MENU_MAIN=1
    MENU_PAUSE=2             # Supposed to be options in the middle of the game
    MENU_INVENTORY=3        # Press inventory then press key to pull up the item menu with options such as [drop, wield, use]
    MENU_EQUIP=4        # You know where you wear that shiny plate mail

    MENU_TARGET_POINT=10  # The cursed thing, but now with keyboard controls instead
    MENU_TARGET_DIR=11    # Nine directions which if self-target (NumPad5 or s) fires to ground

class Factions(Enum):
    # Furniture, environment and items are factionless
    NEUTRAL=0
    ALLY=1
    ENEMY=2

class RenderOrder(Enum):
    # Ground terrain is zero
    ENVIRONMENT=1  # Entity'd terrain, spook trees, etc.
    FURNITURE=2
    ITEM=3          # Including corpses
    ACTOR_SHORT=4
    ACTOR=5
    PARTICLE=6