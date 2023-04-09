import math


class Coords:
    def __init__(self, id, long, lat):
        self.id = id
        self.long = long
        self.lat = lat


class Route:
    def __init__(self, route=None):
        if route is None:
            route = []
        self.route = route
        self.distance = 0

    def calculate_route_distance(self) -> None:
        route_distance = 0
        for point in range(len(self.route)):
            if point + 1 < len(self.route):
                distance = calc_distance_between_points(self.route[point], self.route[point + 1])
            else:
                distance = calc_distance_between_points(self.route[point], self.route[0])
            route_distance += distance

        self.distance = route_distance


def calc_distance_between_points(point_1: Coords, point_2: Coords) -> int:
    p1 = [point_1.lat, point_1.long]
    p2 = [point_2.lat, point_2.long]
    return math.dist(p1, p2)
