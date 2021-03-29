import numpy as np
import math
import matplotlib.pyplot as plt


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

            if generation % 50 == 0:
                print(f"Generation: {generation}")
                # print(
                #     f"Best individual and fitness: {best_individual}, {best_fitness}")
                self.plot_graph(generation, population)

            if best_fitness < -106.764536:
                break

            # Create the next generation
            Q = np.zeros((self.pop_size, 2))
            for i in range(math.floor(self.pop_size / 2)):
                parent1 = self.selection(population)
                parent2 = self.selection(population)

                c1, c2 = self.average_crossover(parent1, parent2)

                Q[2 * i] = self.mutate(c1)
                Q[2 * i + 1] = self.mutate(c2)

            population = Q
            generation += 1

        self.plot_graph(generation, population)
        return generation, best_individual, best_fitness

    def fitness(self, individual):
        x = individual[0]
        y = individual[1]

        aux1 = np.power(1 - np.cos(y), 2)
        aux2 = np.power(1 - np.sin(x), 2)

        fitness = np.sin(x) * np.exp(aux1) + np.cos(y) * \
            np.exp(aux2) + np.power((x-y), 2)

        return fitness

    def selection(self, population):
        return population[np.random.randint(self.pop_size)]

    def average_crossover(self, parent1, parent2):
        c1 = [(parent1[0] + parent2[0]) / 2, (parent1[1] + parent2[1]) / 2]

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

    def plot_graph(self, generation, population):
        # plotting the points 
        plt.plot(population.T[0], population.T[1], color='blue', linestyle='none', linewidth = 3,
                 marker='o', markersize=12)
          
        # setting x and y axis range
        plt.ylim(-10,10)
        plt.xlim(-10,10)
          
        # naming the axis
        plt.xlabel('x')
        plt.ylabel('y')
          
        # giving a title to my graph
        plt.title(f'Inididuals from generation {generation}')
          
        # function to show the plot
        plt.show()
