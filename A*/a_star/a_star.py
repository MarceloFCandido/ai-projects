import numpy as np


class A_Star(object):
    def __init__(self, objective, heuristics_filename, real_distances_filename):
        self.objective = objective
        self.heuristics = np.genfromtxt(
            heuristics_filename, delimiter=",")
        self.real_distances = np.genfromtxt(
            real_distances_filename, delimiter=",")

        self.paths = [[{"id": self.objective[0],
                        "straight_line_distance": self.heuristics[self.objective[0], self.objective[1]]}]]

    def run(self):
        print(self.heuristics)
        print(self.real_distances)
        print(self.paths)
