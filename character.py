from spell import Spell

class Character:
    def __init__(self, name, health, mana, spells):
        self.name = name
        self.health = health
        self.mana = mana
        self.spells = spells

    def cast_spell(self, spell, target):
        if spell not in self.spells:
            print(f"{self.name} doesn't have spell {spell.name}")
            return False
        if not spell.can_cast():
            print(f"Spell {spell.name} is on cooldown.")
            return False
        if self.mana < spell.mana_cost:
            print(f"Not enough mana to cast {spell.name}.")
            return False
        spell.cast()
        self.mana -= spell.mana_cost
        target.health -= spell.damage
        print(f"{self.name} cast {spell.name} on {target.name} causing {spell.damage} damage!")
        return True

    def meditate(self):
        self.mana += 10
        if self.mana > 100:
            self.mana = 100

def create_character(name):
    if name == "Geralt":
        spells = [
            Spell("Igni", 20, 25, 5),
            Spell("Aard", 15, 20, 3),
            Spell("Quen Shield", 25, 0, 10),
            Spell("Yrden Trap", 20, 15, 8),
            Spell("Axii Charm", 15, 10, 6)
        ]
        return Character("Geralt", 100, 100, spells)
    elif name == "Yennefer":
        spells = [
            Spell("Fireball", 25, 30, 4),
            Spell("Teleport", 30, 0, 6),
            Spell("Magic Shield", 20, 0, 9)
        ]
        return Character("Yennefer", 90, 120, spells)
    elif name == "Golem":
        spells = [
            Spell("Smash", 10, 35, 6),
            Spell("Stomp", 5, 20, 2),
            Spell("Earthquake", 20, 30, 8),
            Spell("Stone Skin", 15, 0, 10),
            Spell("Rock Throw", 10, 15, 4)
        ]
        return Character("Golem", 95, 50, spells)
    elif name == "Obsidian Brute":
        spells = [
            Spell("Obsidian Punch", 20, 30, 4),
            Spell("Shadow Slam", 25, 20, 6),
            Spell("Rage Roar", 15, 0, 8)
        ]
        return Character("Obsidian Brute", 85, 40, spells)
    elif name == "Crystal Witch":
        spells = [
            Spell("Mana Drain", 10, 0, 3),
            Spell("Ice Shard", 20, 25, 5),
            Spell("Crystal Armor", 30, 0, 10)
        ]
        return Character("Crystal Witch", 70, 150, spells)
    elif name == "Iron Fang Beast":
        spells = [
            Spell("Savage Bite", 15, 35, 4),
            Spell("Claw Swipe", 10, 15, 2),
            Spell("Howl of Fury", 20, 0, 6)
        ]
        return Character("Iron Fang Beast", 60, 30, spells)
    else:
        return Character("Unknown", 50, 50, [])
