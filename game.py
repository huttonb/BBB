from wizard import Wizard
from firebolt import FireBolt


class Game():
        def __init__(self):
            self.wizard_one = Wizard()
            self.wizard_two = Wizard()
            self.game_field = None #TODO: Create Game Field
            self.turn = 0
            self.start_game()

        def start_game(self):
            wizard_one_spell = self.choose_spell(self.wizard_one)
            wizard_two_spell = self.choose_spell(self.wizard_two)
            if wizard_one_spell.get_cast_time() > wizard_two_spell.get_cast_time():
                pass
            elif wizard_one_spell.get_cast_time() < wizard_two_spell.get_cast_time():


        def cast_spell(self, wizard, spell):
            pass



        """ This is a temporary function for testing. Eventually choose spell will be comprised of
        the players choice of spell, and the AI's choice."""
        def choose_spell(self, wizard):
            spell = FireBolt
            return spell
