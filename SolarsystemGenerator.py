import json
import random
from AstronomicalObjects import SolarSystem, Star

from GalaxyGenerator import NameGenerator
from PlanetGenerator import PlanetGenerator

import numpy as np

class SolarSystemGenerator:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)
            self.planet_generator = PlanetGenerator(self.config)

    def generate_position(self, existing_positions):
        while True:
            position = np.random.uniform(-1, 1, 3)  # 3D position
            position *= np.random.uniform(self.config['solar_systems']['min_distance'],
                                          self.config['solar_systems']['max_distance'])
            if all(np.linalg.norm(np.array(position) - np.array(pos)) >= self.config['solar_systems']['min_distance']
                   for pos in existing_positions):
                return position.tolist()

    def generate_solar_system(self, galaxy_name, existing_positions):
        solar_system_name = NameGenerator.generate_name(f'SolarSystem_{galaxy_name}')
        position = self.generate_position(existing_positions)
        existing_positions.append(position)
        solar_system = SolarSystem(solar_system_name, position=position)
        # Generate the central star
        star_name = NameGenerator.generate_name('Star')
        star = Star(name=star_name)
        solar_system.add_celestial_object(star)
        # Generate planets
        for _ in range(random.randint(self.config['planets']['min'], self.config['planets']['max'])):
            planet = self.planet_generator.generate_planet(star)
            solar_system.add_celestial_object(planet)
        return solar_system

