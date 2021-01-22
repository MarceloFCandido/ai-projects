import numpy as np


class A_Star(object):
    def __init__(self, objective, heuristics_filename, real_distances_filename):
        self.objective = objective
        self.heuristics = np.genfromtxt(
            heuristics_filename, delimiter=",")
        self.real_distances = np.genfromtxt(
            real_distances_filename, delimiter=",")

        self.paths = [[self.create_node(
            self.objective[0], 0, self.heuristics[self.objective[0], self.objective[1]])]]

    def create_node(self, id, current_path_length, heuristics_value):
        return {"id": id,
                "current_path_length": current_path_length,
                "heuristics_value": heuristics_value,
                "visited": False}

    def compare_paths(self, path):
        for path_for_comparison in self.paths:
            if path[-1]["id"] == path_for_comparison[-1]["id"]:
                continue
            elif path[-1]["current_path_length"] + path[-1]["heuristics_value"] > path_for_comparison[-1]["current_path_length"] + path_for_comparison[-1]["heuristics_value"]:
                return False
        return True

    def verify_achieved_objective(self):
        for path in self.paths:
            if path[-1]["id"] == self.objective[1]:
                if self.compare_paths(path[-1]):
                    return True
                else:
                    return False
        return False

    def choose_next(self):
        next = 0
        smallest = self.paths[next][-1]["current_path_length"] + \
            self.paths[next][-1]["heuristics_value"]

        for i, path in enumerate(self.paths):
            if path[-1]["current_path_length"] + path[-1]["heuristics_value"] < smallest:
                smallest = path[-1]["current_path_length"] + \
                    path[-1]["heuristics_value"]
                next = i

        return next

    def expand_chosen(self, index):
        id = self.paths[index][-1]["id"]

        possibilities = np.nonzero(self.real_distances[id, :])[0]
        print(id, possibilities)

    def run(self):
        while not self.verify_achieved_objective():
            self.expand_chosen(self.choose_next())
