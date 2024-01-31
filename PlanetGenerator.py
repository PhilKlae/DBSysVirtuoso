import random
from AstronomicalObjects import CelestialObject
from GalaxyGenerator import NameGenerator


class MoonGenerator:
    def __init__(self, config):
        self.config = config

    def generate_moons(self, planet):
        num_moons = random.randint(self.config['moons']['min'], self.config['moons']['max'])
        for _ in range(num_moons):
            moon_name = NameGenerator.generate_name(f'Moon_{planet.name}')
            moon = CelestialObject(name=moon_name, center=planet)
            planet.add_moon(moon)

class PlanetGenerator:
    def __init__(self, config):
        self.config = config
        self.moon_generator = MoonGenerator(config)

    def generate_planet(self, star):
        planet_name = NameGenerator.generate_name('Planet')
        planet = CelestialObject(name=planet_name, center=star)
        self.moon_generator.generate_moons(planet)
        return planet
