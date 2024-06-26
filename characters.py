import math

class Character:
    def __init__(self, species, pos_x, pos_y, fight_tendency):
        self.species = species
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.current_velocity = 0
        self.on_edge = False
        self.edge_location = None
        self.max_pos_x = None
        self.min_pos_x = None
        self.max_pos_y = None
        self.min_pos_y = None
        self.max_velocity = None
        self.appearance = None
        self.fight_tendency = fight_tendency
        self.acceleration = self.fight_tendency * 0.5
        self._initialize_species()

    def _initialize_species(self):
        species_relations = {
            'rock': ('scissors', 'paper'),
            'paper': ('rock', 'scissors'),
            'scissors': ('paper', 'rock'),
            'lizard': ('spock', 'rock'),
             'spock': ('scissors', 'lizard')
        }
        if self.species in species_relations:
            self.defeats, self.defeated_by = species_relations[self.species]

    def set_pos_limits(self, min_pos_x, max_pos_x, min_pos_y, max_pos_y):
        self.min_pos_x = min_pos_x
        self.max_pos_x = max_pos_x
        self.min_pos_y = min_pos_y
        self.max_pos_y = max_pos_y
        self._check_location()

    def set_max_velocity(self, max_velocity):
        self.max_velocity = max_velocity

    def move(self, vec_x, vec_y):
        velocity = self._calculate_velocity()
        displacement_x = vec_x * velocity
        displacement_y = vec_y * velocity

        self.pos_x += displacement_x
        self.pos_y += displacement_y

        self._apply_position_limits()
        self._check_location()

    def _calculate_velocity(self):
        self.current_velocity = min(self.current_velocity + self.acceleration, self.max_velocity)
        return self.current_velocity

    def _apply_position_limits(self):
        self.pos_x = max(min(self.pos_x, self.max_pos_x), self.min_pos_x)
        self.pos_y = max(min(self.pos_y, self.max_pos_y), self.min_pos_y)

    def set_appearance(self, appearance):
        self.appearance = appearance

    def _check_location(self):
        self.on_edge = (
            self.pos_x in (self.min_pos_x, self.max_pos_x) or 
            self.pos_y in (self.min_pos_y, self.max_pos_y)
        )
        if self.pos_x == self.min_pos_x:
            self.edge_location = 'left'
        elif self.pos_x == self.max_pos_x:
            self.edge_location = 'right'
        elif self.pos_y == self.min_pos_y:
            self.edge_location = 'top'
        elif self.pos_y == self.max_pos_y:
            self.edge_location = 'bottom'
        else:
            self.edge_location = None

    def rotate(self, vec_x, vec_y, angle):
        angle_rad = math.radians(angle)
        new_x = vec_x * math.cos(angle_rad) - vec_y * math.sin(angle_rad)
        new_y = vec_x * math.sin(angle_rad) + vec_y * math.cos(angle_rad)
        return new_x, new_y
