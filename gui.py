import pygame
from characters import Character
from interactions import Interactions
from stratergies import Stratergies
import random

class Gameplay:
    def __init__(self, number_of_players):
        pygame.init()
        self.number_of_players = number_of_players
        self.number_of_battles = 0
        self.rounds = 0
        self.x_min = 0
        self.x_max = 700
        self.y_min = 0
        self.y_max = 700
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        # Load images for characters
        self.images = {
            'rock': pygame.image.load('rock.png').convert_alpha(),
            'paper': pygame.image.load('paper.png').convert_alpha(),
            'scissors': pygame.image.load('scissors.png').convert_alpha()
            #'lizard': pygame.image.load('lizard.png').convert_alpha(),
            #'spock': pygame.image.load('spock.png').convert_alpha()
        }
        
        # Resize images if necessary
        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key], (30, 30))
        
        self.characters = []
        self.winner = None

    def generate_character(self, char_type):
        pos_x = random.randint(self.x_min, self.x_max)
        pos_y = random.randint(self.y_min, self.y_max)
        fight_tendency = random.random()
        new_char = Character(char_type, pos_x, pos_y, fight_tendency)
        new_char.set_pos_limits(self.x_min, self.x_max, self.y_min, self.y_max)
        new_char.set_max_velocity(random.randint(1, 10))
        return new_char

    def draw_character(self, character):
        image = self.images[character.species]
        self.screen.blit(image, (character.pos_x, character.pos_y))

    def play_game(self):
        print('Game started')
        if self.number_of_players % 3 != 0:
            print('Number of players must be a multiple of 3')
            return
        else:
            for i in range(self.number_of_players // 3):
                self.characters.append(self.generate_character('rock'))
                self.characters.append(self.generate_character('paper'))
                self.characters.append(self.generate_character('scissors'))
                #self.characters.append(self.generate_character('lizard'))
                #self.characters.append(self.generate_character('spock'))

            
            
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                self.screen.fill((255,255,255))
                self.rounds += 1

                for i in range(len(self.characters)):
                    for j in range(i + 1, len(self.characters)):
                        interactions = Interactions(self.characters[i], self.characters[j])
                        interactions.battle_scenarios()
                        self.number_of_battles += 1

                for character in self.characters:
                    # randomly assign a stratergy to each character
                    stratergy = Stratergies(self.characters, character)
                    # randomly assign offense or defese strategy to each character
                    if random.random() < 0.5:
                        stratergy.optimise_survival_offense()
                    else:
                        stratergy.optimise_survival_defense()

                    self.draw_character(character)

                # Check if all characters are of the same species
                if len(set([character.species for character in self.characters])) == 1:
                    self.winner = self.characters[0].species
                    print(f"The winner is {self.winner}")
                    running = False

                pygame.display.flip()
                self.clock.tick(24)

        pygame.quit()

# To start the game
game = Gameplay(60)
game.play_game()
