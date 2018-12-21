class Spell:
    def __init__(self, base_mana = 0):
        self.mana_cost = base_mana # mana cost is how many manalets it costs.
        self.mana_tier = 0 # mana tier is how many orbs of mana
        self.duration = 0 # duration is rounds to live
        self.zone = None # Zone is the current zone that the spell is in

    """ Start Spell is overriden in each child class"""
    def start_spell(self):
        pass

    """ Calculates the mana orb cost based on manalet cost"""
    def _calculate_mana(self):
        self.mana_tier = int((self.mana_cost / 100))
