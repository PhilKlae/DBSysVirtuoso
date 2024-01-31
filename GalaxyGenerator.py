import json
import random
from AstronomicalObjects import Galaxy
from NameGenerator import NameGenerator

from SolarsystemGenerator import SolarSystemGenerator

import numpy as np


class GalaxyGenerator:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)
            self.solar_system_generator = SolarSystemGenerator(config_file)

    def generate_position(self, existing_positions):
        while True:
            position = np.random.uniform(-1, 1, 3)  # 3D position
            position *= np.random.uniform(self.config['galaxy_spacing']['min_distance'],
                                          self.config['galaxy_spacing']['max_distance'])
            if all(np.linalg.norm(np.array(position) - np.array(pos)) >= self.config['galaxy_spacing']['min_distance']
                   for pos in existing_positions):
                return position.tolist()

    def generate_galaxies(self):
        galaxies = []
        existing_positions = []
        for _ in range(self.config['galaxies']):
            position = self.generate_position(existing_positions)
            existing_positions.append(position)
            galaxy_name = NameGenerator.generate_name('Galaxy')
            galaxy = Galaxy(galaxy_name, position=position)
            for _ in range(random.randint(self.config['solar_systems']['min'], self.config['solar_systems']['max'])):
                existing_solar_system_positions = []
                solar_system = self.solar_system_generator.generate_solar_system(galaxy_name,existing_solar_system_positions)
                galaxy.add_solar_system(solar_system)
            galaxies.append(galaxy)
        return galaxies
