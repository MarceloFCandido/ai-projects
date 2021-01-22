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
                "heuristics_value": heuristics_value}

    def compare_paths(self, path):
        for path_for_comparison in self.paths:
            if path[-1]["id"] == path_for_comparison[-1]["id"]:
                continue
            elif path[-1]["current_path_length"] + path[-1]["heuristics_value"] > path_for_comparison[-1]["current_path_length"] + path_for_comparison[-1]["heuristics_value"]:
                return False
        return True

    def verify_loop(self, path, id):
        for node in path:
            if node["id"] == id:
                return True
        return False

    def verify_achieved_objective(self):
        for path in self.paths:
            if path[-1]["id"] == self.objective[1]:
                if self.compare_paths(path):
                    return path
                else:
                    return None
        return None

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
        path_to_expand = self.paths[index].copy()
        self.paths.remove(path_to_expand)

        last_node = path_to_expand[-1]

        possibilities = np.nonzero(
            self.real_distances[last_node["id"], :])[0]

        current_distance = last_node["current_path_length"]
        for possibility in possibilities:
            if self.verify_loop(path_to_expand, possibility):
                continue

            new_path = path_to_expand.copy()

            distance_last_to_current = current_distance + \
                self.real_distances[last_node["id"], possibility]
            heuristics_value = self.heuristics[possibility, self.objective[1]]

            new_path.append(self.create_node(
                possibility, distance_last_to_current, heuristics_value))

            self.paths.append(new_path)

    def run(self):
        path = None

        while path == None:
            chosen = self.choose_next()
            self.expand_chosen(chosen)
            path = self.verify_achieved_objective()

        simplified_path = []
        for id in map(lambda node: node["id"], path):
            simplified_path.append(id)

        path_length = path[-1]["current_path_length"]

        return simplified_path, path_length
