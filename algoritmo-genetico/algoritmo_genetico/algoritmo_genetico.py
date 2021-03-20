import numpy as np
import math

class AlgoritmoGenetico(object):
    def __init__(self, popsize, mutation_rate) -> None:
        super().__init__()

        self.popsize = popsize
        self.mutation_rate = mutation_rate
        
    def bla(self):

        P = np.zeros((self.popsize, 2))

        for i in range(self.popsize):
            # valor aleatório entre -10 e 10
            P[i] = np.random.rand(1, 2) * 20 - 10
        print(P)

        best_ind = []
        best_fit = None

        generation = 0

        while True:
            for ind in P:
                f = self.fitness(ind)

                # objetivo do algoritmo eh minimizar
                print("F\n", self.fitness(ind))
                if best_fit == None or self.fitness(ind) < best_fit:
                    best_ind = ind
                    best_fit = self.fitness(ind)

            Q = np.zeros((self.popsize, 2))
            for i in range(math.floor(self.popsize/2)):
                parent1 = P[2*i]
                parent2 = P[2*i+1]

                c1, c2 = self.crossover_media(parent1, parent2)

                Q[2*i] = self.mutate(c1)
                Q[2*i+1] = self.mutate(c2)

            P = Q
            generation += 1

            print("P: \n", P)
            print("Best: \n", best_ind, best_fit)
            print("Geracao: ", generation)

            # TODO: verificar se esse eh o melhor jeito de parar a funcao
            if best_fit < -100:
                break


    def fitness(self, ind):
        x = ind[0]
        y = ind[1]

        aux1 = np.power(1 - np.cos(y), 2)
        aux2 = np.power(1 - np.sin(x), 2)

        f = np.sin(x)*np.exp(aux1) + np.cos(y)*np.exp(aux2) + np.power((x-y), 2)

        return f

    def crossover_uniforme(self, p1, p2):
        # crossover uniforme
        c1 = [p1[0], p2[1]]
        c2 = [p2[1], p2[0]]

        return c1, c2

    def crossover_media(self, p1, p2):
        # crossover media
        c1 = [ (p1[0] + p2[0])/2, (p1[1] + p2[1])/2]

        #mantem o melhor pai
        if self.fitness(p1) <= self.fitness(p2):
            return c1, p1
        else:
            return c1, p2

    def mutate(self, ind):

        new_ind = ind
        rand_num = np.random.rand(1)[0]
        
        if self.mutation_rate >= rand_num:
            rand_exp = np.random.randint(7)
            rand_op = np.random.randint(4)

            print("M")
            print("ind: ", ind)
            print("num: ", rand_num, " exp: ", rand_exp, " op: ", rand_op)

            if rand_op == 0:
                new_ind[0] = ind[0] + np.power(2, rand_exp)
                new_ind[1] = ind[1] + np.power(2, rand_exp)
            elif rand_op == 1:
                new_ind[0] = ind[0] - np.power(2, rand_exp)
                new_ind[1] = ind[1] + np.power(2, rand_exp)
            elif rand_op == 2:
                new_ind[0] = ind[0] + np.power(2, rand_exp)
                new_ind[1] = ind[1] - np.power(2, rand_exp)
            else:
                new_ind[0] = ind[0] - np.power(2, rand_exp)
                new_ind[1] = ind[1] - np.power(2, rand_exp)

            print("new_ind: ", new_ind )

        return new_ind


