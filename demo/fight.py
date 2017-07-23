class Fight(object):
    def __init__(self, credit_card):
        self._credit_card = credit_card
        self._combatants = []

    def add_combatant(self, combatant):
        self._combatants.push(combatant)
