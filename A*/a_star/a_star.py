import numpy as np


class A_Star(object):
    def __init__(self, objective, heuristics, real_distances):
        self.objective = objective
        self.heuristics = heuristics
        self.real_distances = real_distances

    def run(self):
        pass
