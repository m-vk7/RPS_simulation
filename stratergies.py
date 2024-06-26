from characters import Character
import math

class Stratergies:
    def __init__(self, characters: list, target_char: Character):
        self.characters = characters
        self.target_char = target_char

    def __find_nearest_loser(self):
        losers_list = [loser for loser in self.characters if loser.defeated_by == self.target_char.species]
        if len(losers_list) == 0:
            return None, None
        else:
            nearest_loser = min(losers_list, key=lambda loser: self.__distance(loser.pos_x, loser.pos_y, self.target_char.pos_x, self.target_char.pos_y))
            return nearest_loser.pos_x, nearest_loser.pos_y

    def __find_nearest_killer(self):
        killers_list = [killer for killer in self.characters if killer.defeats == self.target_char.species]
        if len(killers_list) == 0:
            return None, None
        else:
            nearest_killer = min(killers_list, key=lambda killer: self.__distance(killer.pos_x, killer.pos_y, self.target_char.pos_x, self.target_char.pos_y))
            return nearest_killer.pos_x, nearest_killer.pos_y

    def __distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def __calculate_vector(self, target_x, target_y):
        vec_x = target_x - self.target_char.pos_x
        vec_y = target_y - self.target_char.pos_y
        magnitude = math.sqrt(vec_x**2 + vec_y**2)
        if magnitude == 0:
            return 0, 0
        return vec_x / magnitude, vec_y / magnitude

    def __rotate_character(self, angle):
        angle_radians = math.radians(angle)
        new_vec_x, new_vec_y = self.target_char.rotate(1, 0, angle)
        self.target_char.move(new_vec_x, new_vec_y)

    def __is_corner(self):
        return (
            (self.target_char.pos_x == self.target_char.min_pos_x and self.target_char.pos_y == self.target_char.min_pos_y) or
            (self.target_char.pos_x == self.target_char.max_pos_x and self.target_char.pos_y == self.target_char.min_pos_y) or
            (self.target_char.pos_x == self.target_char.min_pos_x and self.target_char.pos_y == self.target_char.max_pos_y) or
            (self.target_char.pos_x == self.target_char.max_pos_x and self.target_char.pos_y == self.target_char.max_pos_y)
        )

    def __move_away_from_corner(self):
        if self.target_char.pos_x == self.target_char.min_pos_x:
            move_x = 1
        elif self.target_char.pos_x == self.target_char.max_pos_x:
            move_x = -1
        else:
            move_x = 0

        if self.target_char.pos_y == self.target_char.min_pos_y:
            move_y = 1
        elif self.target_char.pos_y == self.target_char.max_pos_y:
            move_y = -1
        else:
            move_y = 0

        self.target_char.move(move_x, move_y)

    def optimise_survival_offense(self):
        loser_x, loser_y = self.__find_nearest_loser()
        if loser_x is not None and loser_y is not None:
            vec_x, vec_y = self.__calculate_vector(loser_x, loser_y)
            self.target_char.move(vec_x, vec_y)
        else:
            killer_x, killer_y = self.__find_nearest_killer()
            if killer_x is not None and killer_y is not None:
                vec_x, vec_y = self.__calculate_vector(killer_x, killer_y)
                self.target_char.move(-vec_x, -vec_y)

        if self.__is_corner():
            self.__move_away_from_corner()
        elif self.target_char.on_edge:
            if loser_x is not None and loser_y is not None:
                target_x, target_y = loser_x, loser_y
            elif killer_x is not None and killer_y is not None:
                target_x, target_y = -killer_x, -killer_y
            else:
                return
            
            vec_x, vec_y = self.__calculate_vector(target_x, target_y)
            angle = math.degrees(math.atan2(vec_y, vec_x))
            self.__rotate_character(angle)

    def optimise_survival_defense(self):
        killer_x, killer_y = self.__find_nearest_killer()
        if killer_x is not None and killer_y is not None:
            vec_x, vec_y = self.__calculate_vector(killer_x, killer_y)
            self.target_char.move(-vec_x, -vec_y)
        else:
            loser_x, loser_y = self.__find_nearest_loser()
            if loser_x is not None and loser_y is not None:
                vec_x, vec_y = self.__calculate_vector(loser_x, loser_y)
                self.target_char.move(vec_x, vec_y)

        if self.__is_corner():
            self.__move_away_from_corner()
        elif self.target_char.on_edge:
            if killer_x is not None and killer_y is not None:
                target_x, target_y = -killer_x, -killer_y
            elif loser_x is not None and loser_y is not None:
                target_x, target_y = loser_x, loser_y
            else:
                return 

            vec_x, vec_y = self.__calculate_vector(target_x, target_y)
            angle = math.degrees(math.atan2(vec_y, vec_x))
            self.__rotate_character(angle)
