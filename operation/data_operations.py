import math
import random
from typing import List

from operation.coords import Coords, Route


def generate_population(table, pop_number):
    population = []
    for i in range(pop_number):
        data_to_shuffle = Route(table.copy())
        random.shuffle(data_to_shuffle.route)
        population.append(data_to_shuffle)
    return population


def sort_population(population):
    for pop in population:
        pop.calculate_route_distance()
    return sorted(population, key=lambda x: x.distance, reverse=False)