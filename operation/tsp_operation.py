import random

from operation.coords import Route


def selection(population, elisism):
    new_selection = []
    for i in range(elisism):
        new_selection.append(population[i])

    for i in range(len(population) - elisism):
        new_selection.append(random.choice(population))

    return new_selection


def crossover(parent1, parent2):
    child = Route()
    mutarion_start = random.randint(0,len(parent1.route))
    mutarion_end = random.randint(0, len(parent1.route))

    if mutarion_start > mutarion_end:
        mutation_swap = mutarion_end
        mutarion_end = mutarion_start
        mutarion_start = mutation_swap

    for i in range(len(parent1.route)):
        child.route.append(None)

    for i in range(mutarion_start, mutarion_end):
        child.route[i] = parent1.route[i]

    for i in range(len(parent2.route)):
        # if parent2 has a city that the child doesn't have yet:
        if not parent2.route[i] in child.route:
            # it puts it in the first 'None' spot and breaks out of the loop.
            for x in range(len(child.route)):
                if child.route[x] is None:
                    child.route[x] = parent2.route[i]
                    break
    return child


def mutation(child, mutation_rate):
    for swap in range(len(child.route)):
        if random.random() < mutation_rate:
            swap_source = random.randint(0, len(child.route)-1)
            swap_start = child.route[swap]
            swap_end = child.route[swap_source]
            child.route[swap] = swap_end
            child.route[swap_source] = swap_start
    return child




