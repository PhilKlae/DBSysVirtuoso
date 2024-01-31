import time
from AstronomicalObjects import Star, Galaxy, SolarSystem, CelestialObject

from GalaxyGenerator import GalaxyGenerator
from TurtleGenerator import generate_all_turtle_syntax


# Assuming the generator classes and their dependencies are defined in other files or above in the script

def main():
    print("Starting the generation of astronomical entities...")

    # Initialize the Galaxy Generator
    galaxy_generator = GalaxyGenerator('config.json')

    # Generate galaxies
    galaxies = galaxy_generator.generate_galaxies()

    for i, galaxy in enumerate(galaxies, start=1):
        print(f"Generated Galaxy {i}/{len(galaxies)}: {galaxy.name}")
        for j, solar_system in enumerate(galaxy.solar_systems, start=1):
            print(f"  Solar System {j}/{len(galaxy.solar_systems)} in {galaxy.name}: {solar_system.name}")
            for k, celestial_object in enumerate(solar_system.celestial_objects, start=1):
                if isinstance(celestial_object, Star):
                    print(f"    Star in {solar_system.name}: {celestial_object.name}")
                else:
                    print(f"    Planet {k}/{len(solar_system.celestial_objects)-1} in {solar_system.name}: {celestial_object.name}")
                    for l, moon in enumerate(celestial_object.moons, start=1):
                        print(f"      Moon {l}/{len(celestial_object.moons)} of {celestial_object.name}: {moon.name}")

    print("Generation complete!")

    # Generate Turtle syntax for all galaxies
    all_turtle_data = generate_all_turtle_syntax(galaxies)

    # Write the Turtle data to a file
    with open('astronomy_data.ttl', 'w') as file:
        file.write(all_turtle_data)


if __name__ == "__main__":
    main()
