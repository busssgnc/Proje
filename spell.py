import time

class Spell:
    def __init__(self, name, mana_cost, damage, cooldown):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.cooldown = cooldown
        self.last_cast_time = 0

    def can_cast(self):
        return (time.time() - self.last_cast_time) >= self.cooldown

    def cast(self):
        self.last_cast_time = time.time()
