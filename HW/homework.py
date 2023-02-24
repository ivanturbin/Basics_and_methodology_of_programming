import math


def d(mass, radius):
    G = 6.6743 * math.pow(10, -11)
    mass_earth = 5.97600 * math.pow(10, 24)

    return G * mass_earth * mass / radius ** 2


mass = float(input())
radius = float(input())
print(d(mass, radius))