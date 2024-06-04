'''

In this challenge, you have to convert a weight weighed on a planet of the Solar System to the corresponding weight
on another planet.

To convert the weight, you have to divide it by the gravitational force of the planet on which is weighed and
multiply the result (the mass) for the gravitational force of the other planet. See the table below for a list of
gravitational forces:

weight on planet_a / gravitational force of planet_a * gravitational force of planet_b
Planet	m/s²
Mercury	3.7
Venus	8.87
Earth	9.81
Mars	3.711
Jupiter	24.79
Saturn	10.44
Uranus	8.69
Neptune	11.15

Given a weight weighed on planet_a, return the converted value for planet_b rounded to the nearest hundredth.

'''


def space_weights(planet_a, weight, planet_b):
    planets = {"Mercury": 3.7,
               "Venus": 8.87,
               "Earth": 9.81,
               "Mars": 3.711,
               "Jupiter": 24.79,
               "Saturn": 10.44,
               "Uranus": 8.69,
               "Neptune": 11.15}

    return round(weight / planets[planet_a] * planets[planet_b], 2)
