from characters import Character

class Interactions:
    def __init__(self, character1: Character, character2: Character):
        self.character1 = character1
        self.character2 = character2

    def battle(self):
        if self.character1.defeats == self.character2.species:
            self.character2.species = self.character1.species
            self.character2.fight_tendency = self.character1.fight_tendency
            self.character2.defeats = self.character1.defeats
            self.character2.defeated_by = self.character1.defeated_by
            self.character2.appearance = self.character1.appearance      
        elif self.character2.defeats == self.character1.species:
            self.character1.species = self.character2.species
            self.character1.fight_tendency = self.character2.fight_tendency
            self.character1.defeats = self.character2.defeats
            self.character1.defeated_by = self.character2.defeated_by
            self.character1.appearance = self.character2.appearance
        else:
            self.character1.fight_tendency += 0.1
            self.character2.fight_tendency += 0.1

    def distance(self):
        return ((self.character1.pos_x - self.character2.pos_x)**2 + (self.character1.pos_y - self.character2.pos_y)**2)**0.5

    def battle_scenarios(self):
        if self.distance() < 20:
            if self.character1.fight_tendency and self.character2.fight_tendency > 0.5:
                self.battle()
            elif self.character1.fight_tendency or self.character2.fight_tendency > 0.85:
                self.battle()