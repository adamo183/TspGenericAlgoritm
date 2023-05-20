import random
import time

import tsplib95

from operation.data import open_tsp_file, read_config_file, print_result
from operation.data_operations import generate_population, sort_population
from operation.tsp_operation import crossover, selection, mutation


if __name__ == '__main__':
    config = read_config_file()
    data = open_tsp_file(config.data_path)
    population = generate_population(data, config.population_size)
    population = sort_population(population)
    start = time.time()
    current_time = 0
    current_iteration = 0
    while current_iteration < config.iteration:
        random.shuffle(population)
        parents = selection(population, config.population_size_parents)
        children = []
        for _ in range(config.population_size_child):
            candidate = random.sample(parents, 2)
            candidate_children = crossover(candidate[0], candidate[1])
            new_child = mutation(candidate_children, config.mutation_rate)
            children.append(new_child)

        candidates = population + children
        population = sort_population(candidates)
        population = population[0:config.population_size]
        current_time = time.time() - start
        current_iteration +=1
    min_route = population[0]
    print("Minimum calculated route for " + str(config.data_path))
    print(min_route.distance)
    if config.display_route:
        print([str(x.id) + ' (' + str(x.long) + ';' + str(x.lat) + ')' for x in min_route.route])
        print('Calculate time:' + str(current_time))
    if config.display_map:
        print_result(min_route)







    

