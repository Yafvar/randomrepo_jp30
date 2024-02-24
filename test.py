import numpy as np
import random
import matplotlib.pyplot as plt
class Skill_damage_hit():
    def __init__(self, hero: 'Entity',target:'Entity'):

        self.hero = hero
        self.target = target

    def perform_effects(self, attacker: 'Entity'):
        self.damage_effect(self.target)
        print(self.damage_effect(self.target))
        print(f"{attacker.name} did something")
    def damage_effect(self, defender: 'Entity'):
        damage = self.hero.atk - defender.obr
        return max(0, defender.hp - damage)


class Entity():
    def __init__(self, name: str = "None", atk: int = 10, obr: int = 5, hp: int = 100, position: int = 0):
        self.name = name
        self.slot = Arena_slot(position)
        self.obr = obr
        self.atk = atk
        self.hp = hp
        self.basic_skill = Skill_damage_hit(self)

        self.use_skill()

    def use_skill(self):
        self.slot.list_of_actions.append(self.basic_skill)

class Hero(Entity):
    def __init__(self):
        super().__init__()
        self.basic_skill = Skill_damage_hit(self,)

class Enemy(Entity):
    pass
class Arena_slot():
    def __init__(self, id: int):
        self.list_of_actions = []
        self.id = id

class Arena():
    def __init__(self, boss: 'Entity', heroes: list):
        self.heroes = heroes
        self.boss = boss
        self.entities = self.heroes.copy()
        self.entities.append(self.boss)

    def perform_turn(self, turn_number: int):
        for entity in self.entities:
            for action in entity.slot.list_of_actions[turn_number]:
                action.perform_effects(entity)

mag = Entity("Merlin", 20, 5, 70, 1)
barb = Entity("Ragnar", 10, 9, 120, 2)
heroes = [mag, barb]
boss = Entity("pajonk", 10, 5, 200, 7)

arena = Arena(boss, heroes)
arena.perform_turn(0)

