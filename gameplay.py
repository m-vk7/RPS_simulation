from characters import Character
from interactions import Interactions
import random
# generate the same number of characters for each type. Assign each character a random position that is more than the min x and y values and less than the max x and y values and a random fight tendency between 0 and 1.

class Gameplay:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.number_of_battles = 0
        self.rounds = 0
        self.x_min = 0
        self.x_max = 100
        self.y_min = 0
        self.y_max = 100
    
    def generate_character(self,char_type):
        pos_x = random.randint(self.x_min, self.x_max)
        pos_y = random.randint(self.y_min, self.y_max)
        fight_tendency = random.random()
        
        return Character(char_type, pos_x, pos_y, fight_tendency)
   
    def play_game(self):
        print('Game started')
        if self.number_of_players % 3 != 0: 
            print('Number of players must be a multiple of 3')
            return None
        else:
            characters = []
            for i in range(self.number_of_players//3):
                characters.append(self.generate_character('rock'))
                characters.append(self.generate_character('paper'))
                characters.append(self.generate_character('scissors'))

            # in each round, check if a battle scenario occurs between any two characters, and if so, execute the battle, then move the characters, and increment the number of rounds, and repeat until there are characters of only one type left.
            while len(set([character.type for character in characters])) > 1:
                self.rounds += 1
                print(f'Round: {self.rounds}, Battles: {self.number_of_battles}')
                for i in range(len(characters)):
                    for j in range(i+1,len(characters)):
                        interactions = Interactions(characters[i],characters[j])
                        if interactions.distance() < 1:
                            interactions.battle_scenarios()
                            self.number_of_battles += 1
                for character in characters:
                    character.move(random.randint(-20,20),random.randint(-20,20))
            print(f'Game finished in {self.rounds} rounds and {self.number_of_battles} battles. The winner is {characters[0].type}')

game = Gameplay(30)
game.play_game()
