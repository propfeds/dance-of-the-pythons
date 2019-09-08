import tcod
import tcod.path
from numpy import bitwise_or
from enums import Factions, RenderOrder

#pylint: disable=no-member

class Entity:
    def __init__(self, x, y, name, faction, char, colour, hp_max, attack, shield, render_order=RenderOrder.CORPSE, walkable=True, inventory=None, ai=None, item=None, environment=None):
        self.x=x
        self.y=y
        self.name=name
        self.faction=faction
        self.char=char
        self.colour=colour

        self.hp_max=hp_max
        self.hp=hp_max
        self.attack=attack
        self.shield=shield

        self.render_order=render_order
        # Is pathable and not the ability to walk
        self.walkable=walkable
        # Whether the entity has an inventory, is an item or has an AI (if not then furniture)
        self.inventory=inventory
        if self.inventory:
            self.inventory.owner=self
        self.ai=ai
        if self.ai:
            self.ai.owner=self
        self.item=item
        if self.item:
            self.item.owner=self
        self.environment=environment
        if self.environment:
            self.environment.owner=self

    def take_damage(self, damage_amount, piercing, lethal):
        damage_remaining=damage_amount
        # bool is for announcements
        damage_shielded=0
        death=False
        if not piercing:
            if damage_remaining>self.shield:
                damage_shielded=self.shield
                damage_remaining-=self.shield
                self.shield=0
            else:
                damage_shielded=damage_remaining
                self.shield-=damage_remaining
                damage_remaining=0
        if lethal:
            if damage_remaining>self.hp:
                damage_remaining-=self.hp
                self.hp=0
                death=True
            else:
                self.hp-=damage_remaining
                damage_remaining=0
        else:
            if damage_remaining>self.hp-1:
                damage_remaining-=(self.hp-1)
                self.hp=1
            else:
                self.hp-=damage_remaining
                damage_remaining=0
        # returning damage taken
        results=[]
        results.append({'damage_taken': damage_amount-damage_remaining})
        results.extend({'shielded': damage_shielded})
        if death:
            results.append({'dead': self})
        return results

    def deal_damage(self, target, damage_amount, piercing, lethal):
        results=[]
        results.append({'attacker': self.name})
        results.extend({'defender': target})
        results.extend(target.take_damage(damage_amount, piercing, lethal))
        return results

    def move(self, dx, dy, block_map):
        if not self.walkable:
            block_map[self.y, self.x]=False
        self.x+=dx
        self.y+=dy
        if not self.walkable:
            block_map[self.y, self.x]=(not self.walkable)
        return {'move': (dx, dy)}

    def swap(self, target):
        x=self.x
        y=self.y
        self.x=target.x
        self.y=target.y
        target.x=x
        target.y=y
        return {'swap': target}
    
    def get_astar_path(self, path_map, block_map):
        return tcod.path.AStar(bitwise_or(path_map, block_map))
    
    def distance(self, target_x, target_y):
        return max(abs(target_x-self.x), abs(target_y-self.y))

    def bump(self, target):
        return self.deal_damage(target, self.attack, False, True)

    # swappable: True for player, and generally True for leaders/massive ones
    def handle_move(self, dx, dy, spawner, path_map, swappable):
        results=[]
        if dx==0 and dy==0:
            results.extend({'wait': True})
        else:
            response=spawner.check_collision(self.x+dx, self.y+dy, path_map)
            target=response.get('collide')
            if target:
                # Depends on object: if enemy attack, if ally swap (sneks not gonna brek cuz they pathable)
                if target.faction==Factions.NEUTRAL:
                    # Cases for neutral tame and aggro
                    print('PETA')
                elif target.faction!=self.faction:
                    if target.name=='vendor':
                        print('And also storytellers please')
                    else:
                        results.extend(self.bump(target))
                else:
                    # ALLIES: if player is in mouse form or sth they'll phase into the ally else they swap
                    if (not self.walkable) and (not target.walkable) and swappable:
                        results.extend(self.swap(target))
                    else:
                        results.extend(self.move(dx, dy, spawner.block_map))
            elif (not response.get('blocked')) and (not response.get('outofbounds')):
                results.extend(self.move(dx, dy, spawner.block_map))
            # Else player is blocked! And fucntion returns nothing
        return results
        # Fov will be recomputed if you swap or move
        # If function returns nothing (entity is blocked) then don't consume turn (fov_recompute and game_state change happens together on the player)