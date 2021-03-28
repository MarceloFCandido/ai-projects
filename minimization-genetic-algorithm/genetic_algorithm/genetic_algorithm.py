import numpy as np
import math


class GA(object):
    def __init__(self, pop_size, mutation_rate) -> None:
        super().__init__()

        self.pop_size = pop_size
        self.mutation_rate = mutation_rate


    def run(self):
        population = np.zeros((self.pop_size, 2))

        for i in range(self.pop_size):
            # Random number between -10 and 10
            population[i] = np.random.rand(1, 2) * 20 - 10

        best_individual = []
        best_fitness = None

        generation = 0

        while True:
            # Find best fitness of this generation
            for individual in population:
                fitness = self.fitness(individual)

                if best_fitness == None or fitness < best_fitness:
                    best_individual = individual
                    best_fitness = fitness

            # Create the next generation
            Q = np.zeros((self.pop_size, 2))
            for i in range(math.floor(self.pop_size/2)):
                parent1 = self.selection(population)
                parent2 = self.selection(population)

                c1, c2 = self.average_crossover(parent1, parent2)

                Q[2*i] = self.mutate(c1)
                Q[2*i+1] = self.mutate(c2)

            population = Q

            print(f"Generation: {generation}")
            print(f"Best individual and fitness: {best_individual}, {best_fitness}")

            if best_fitness < -106.764536:
                break

            generation += 1

        return generation, best_individual, best_fitness

    def fitness(self, individual):
        x = individual[0]
        y = individual[1]

        aux1 = np.power(1 - np.cos(y), 2)
        aux2 = np.power(1 - np.sin(x), 2)

        fitness = np.sin(x) * np.exp(aux1) + np.cos(y) * \
                  np.exp(aux2) + np.power((x-y), 2)

        return fitness

    def proportional_fitness(self, population, i):
        den = 0
        for individual in population:
            den += self.fitness(individual) + 106.764536

        # nom = 1/(1 + self.fitness(population[i]) + 106.764536)
        nom = self.fitness(population[i]) + 106.764536

        p_fitness = nom/den
        return p_fitness

    def selection(self, population):
        index = 0

        p_fitness = self.proportional_fitness(population, index)
        print(p_fitness)

        total = p_fitness
        random_num = np.random.rand()
        print(random_num)

        while total < random_num:
            index += 1
            total += self.proportional_fitness(population, index)

        print(index)
        print('\n')

        return population[index]

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
            rand_exp = np.random.randint(4)
            rand_op = np.random.randint(4)

            # print("Mutating...")
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

            # print(f"New individual: {new_individual}")

        return new_individual
