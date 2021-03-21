import numpy as np
import math


class GA(object):
    def __init__(self, pop_size, mutation_rate) -> None:
        super().__init__()

        self.pop_size = pop_size
        self.mutation_rate = mutation_rate

    def run(self):
        P = np.zeros((self.pop_size, 2))

        for i in range(self.pop_size):
            P[i] = np.random.rand(1, 2) * 20 - 10

        best_individual = []
        best_fit = None

        generation = 0

        while True:
            for individual in P:
                fitness = self.fitness(individual)

                if best_fit == None or fitness < best_fit:
                    best_individual = individual
                    best_fit = fitness

            Q = np.zeros((self.pop_size, 2))
            for i in range(math.floor(self.pop_size/2)):
                parent1 = P[2*i]
                parent2 = P[2*i+1]

                c1, c2 = self.average_crossover(parent1, parent2)

                Q[2*i] = self.mutate(c1)
                Q[2*i+1] = self.mutate(c2)

            P = Q

            print(f"Generation: {generation}")
            print(
                f"Best individual and fitness: {best_individual}, {best_fit}")

            # TODO: verificar se esse eh o melhor jeito de parar a funcao
            if best_fit < -106.764536:
                break

            generation += 1

    def fitness(self, individual):
        x = individual[0]
        y = individual[1]

        aux1 = np.power(1 - np.cos(y), 2)
        aux2 = np.power(1 - np.sin(x), 2)

        f = np.sin(x) * np.exp(aux1) + np.cos(y) * \
            np.exp(aux2) + np.power((x-y), 2)

        return f

    def uniform_crossover(self, parent1, parent2):
        c1 = [parent1[0], parent2[1]]
        c2 = [parent2[1], parent2[0]]

        return c1, c2

    def average_crossover(self, parent1, parent2):
        c1 = [(parent1[0] + parent2[0])/2, (parent1[1] + parent2[1])/2]

        if self.fitness(parent1) <= self.fitness(parent2):
            return c1, parent1
        else:
            return c1, parent2

    def mutate(self, individual):
        new_individual = individual
        rand_num = np.random.rand(1)[0]

        if self.mutation_rate >= rand_num:
            rand_exp = np.random.randint(7)
            rand_op = np.random.randint(4)

            print("Mutating...")
            if rand_op == 0:
                new_individual[0] = individual[0] + np.power(2, rand_exp)
                new_individual[1] = individual[1] + np.power(2, rand_exp)
            elif rand_op == 1:
                new_individual[0] = individual[0] - np.power(2, rand_exp)
                new_individual[1] = individual[1] + np.power(2, rand_exp)
            elif rand_op == 2:
                new_individual[0] = individual[0] + np.power(2, rand_exp)
                new_individual[1] = individual[1] - np.power(2, rand_exp)
            else:
                new_individual[0] = individual[0] - np.power(2, rand_exp)
                new_individual[1] = individual[1] - np.power(2, rand_exp)

            print(f"New individual: {new_individual}")

        return new_individual
