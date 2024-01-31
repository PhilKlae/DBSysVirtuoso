from AstronomicalObjects import Galaxy, SolarSystem, CelestialObject, Star


def generate_turtle_syntax(entity, base_uri="http://example.org/"):
    turtle_str = ""

    if isinstance(entity, Galaxy):
        galaxy_uri = f"{base_uri}galaxy/{entity.name}"
        turtle_str += f'<{galaxy_uri}> rdf:type astro:Galaxy ;\n'
        turtle_str += f'    astro:name "{entity.name}" ;\n'
        turtle_str += f'    astro:position "X:{entity.position[0]}, Y:{entity.position[1]}, Z:{entity.position[2]}" ;\n'
        for solar_system in entity.solar_systems:
            ss_uri = f"{base_uri}solarsystem/{solar_system.name}"
            turtle_str += f'    astro:contains <{ss_uri}> ;\n'

        turtle_str += "    .\n";

        for solar_system in entity.solar_systems:
            turtle_str += f'<{ss_uri}> astro:isPartOf <{galaxy_uri}> .\n'
            turtle_str += generate_turtle_syntax(solar_system)

    elif isinstance(entity, SolarSystem):
        ss_uri = f"{base_uri}solarsystem/{entity.name}"
        turtle_str += f'<{ss_uri}> rdf:type astro:SolarSystem ;\n'
        turtle_str += f'    astro:name "{entity.name}" ;\n'
        turtle_str += f'    astro:position "X:{entity.position[0]}, Y:{entity.position[1]}, Z:{entity.position[2]}" ;\n'
        for planet in entity.celestial_objects:
            planet_uri = f"{base_uri}celestialobject/{planet.name}"
            turtle_str += f'    astro:contains <{planet_uri}> ; #ss contains \n'
        turtle_str += "    .\n";
        for planet in entity.celestial_objects:
            turtle_str += f'<{planet_uri}>\n    astro:isPartOf <{ss_uri}> .\n'
            turtle_str += generate_turtle_syntax(planet)

    elif isinstance(entity, CelestialObject):

        co_uri = f"{base_uri}celestialobject/{entity.name}"

        turtle_str += f'<{co_uri}> rdf:type astro:CelestialObject ;\n'

        turtle_str += f'    astro:name "{entity.name}" ;\n'

        # Check if the celestial object is a Star

        if isinstance(entity, Star):
            turtle_str += f'    astro:isStar true ;\n'

        if entity.center:
            center_uri = f"{base_uri}celestialobject/{entity.center.name}"

            turtle_str += f'    astro:center <{center_uri}> ;\n'

        turtle_str += f'    astro:distanceToCenter {entity.distance_to_center} ;\n'

        turtle_str += f'    astro:mass {entity.mass} ;\n'

        turtle_str += f'    astro:rotationSpeed {entity.rotation_speed} ;\n'

        if entity.image:
            turtle_str += f'    astro:image <{entity.image}> ;\n'

        turtle_str += '    .\n'

        for moon in entity.moons:
            moon_uri = f"{base_uri}celestialobject/{moon.name}"

            turtle_str += f'<{moon_uri}> astro:isPartOf <{co_uri}> .\n'

            turtle_str += generate_turtle_syntax(moon)

    # Add similar cases for Star and Place if needed

    return turtle_str

def generate_all_turtle_syntax(galaxies):
    f = open("turtleprefix", "r")
    all_turtle_data = f.read()
    for galaxy in galaxies:
        all_turtle_data += generate_turtle_syntax(galaxy)
    return all_turtle_data