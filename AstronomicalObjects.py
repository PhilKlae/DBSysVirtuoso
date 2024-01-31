
class CelestialObject:
    def __init__(self, name, center=None, distance_to_center=0, mass=0, rotation_speed=0, image=None):
        self.name = name
        self.center = center  # CelestialObject that this object orbits around
        self.distance_to_center = distance_to_center
        self.mass = mass
        self.rotation_speed = rotation_speed
        self.image = image
        self.moons = []  # Only relevant for planets

    def add_moon(self, moon):
        self.moons.append(moon)

class Place:
    def __init__(self, name, description, image, located_on):
        self.name = name
        self.description = description
        self.image = image
        self.located_on = located_on  # CelestialObject where this place is located

class SolarSystem:
    def __init__(self, name, position=(0, 0, 0)):
        self.name = name
        self.celestial_objects = []  # List of planets and the star
        self.position = position

    def add_celestial_object(self, celestial_object):
        self.celestial_objects.append(celestial_object)

class Galaxy:
    def __init__(self, name, position=(0, 0, 0)):
        self.name = name
        self.solar_systems = []  # List of SolarSystem
        self.position = position

    def add_solar_system(self, solar_system):
        self.solar_systems.append(solar_system)

class Star(CelestialObject):
    def __init__(self, name, mass=0, rotation_speed=0, image=None):
        super().__init__(name, center=None, distance_to_center=0, mass=mass, rotation_speed=rotation_speed, image=image)
