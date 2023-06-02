import tsplib95
from configparser import ConfigParser
from operation.coords import Coords
import pandas as pd
import matplotlib.pyplot as plt


def open_tsp_file(path: str):
    raw_data = tsplib95.load(path)
    coords_array = []
    for node in raw_data.node_coords:
        coords_array.append(Coords(node, raw_data.node_coords[node][0], raw_data.node_coords[node][1]))
    return coords_array


class Config:
    def __init__(self):
        self.data_path = ''
        self.population_size = 0
        self.population_size_child = 0
        self.population_size_parents = 0
        self.mutation_rate = 0
        self.min_accepted_distance = 0
        self.max_calc_time = 0
        self.display_route = True
        self.display_map = True


def read_config_file():
    config = ConfigParser()
    config.read('config.ini')
    conf = Config()
    conf.data_path = config.get('main', 'DATA_PATH')
    conf.population_size = config.getint('main', 'POPULATION_SIZE')
    conf.population_size_child = config.getint('main', 'CHILD_POPULATION_SIZE')
    conf.population_size_parents = config.getint('main', 'PARENTS_POPULATION_SIZE')
    conf.mutation_rate = config.getfloat('main', 'MUTATION_RATE')
    conf.display_route = config.getboolean('main', 'DISPLAY_ROUTE')
    conf.display_map = config.getboolean('main', 'DISPLAY_MAP')
    conf.iteration = config.getint('main', 'ITERATION')
    return conf


def print_result(population):
    data_to_print = []
    for coords in population.route:
        data_to_add = [coords.long, coords.lat]
        data_to_print.append(data_to_add)

    data_to_print.append([population.route[0].long, population.route[0].lat])
    df = pd.DataFrame(data=data_to_print, columns=['x', 'y'])
    df.plot(x='x', y='y')
    plt.show()