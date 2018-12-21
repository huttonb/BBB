import spell

""" Bolt class is the archetype of all bolt spells, such as ForceBolt, FireBolt, etc"""
class Bolt(spell.Spell):
    def __init__(self, base_type, base_potential, base_mana = 10):
        super().__init__(base_mana)
        """ Setting up base cost of bolt """
        self.speed = 1
        self.magic_potential = 1
        self.type = "null"
        self.force = 0

        self.field = None # TODO: Create a field object

    """ calculates damage based off of magic potential, force, and type"""
    def _calculate_damage(self):
        return self.force * self.magic_potential

    """ Bolt Travels calls upon the field class to update its location"""
    def bolt_travel(self):
        self.field.bolt_travel(self.speed)

    def bolt_hit(self):
        effect = self.effect()
        return (self._calculate_damage(), effect)

    """ Effect is a method that you pass to the target hit by the bolt, it determines effects
        beyond just damage, such as setting aflame, or freezing."""
    def effect(target):
        pass
