import sys
from getopt import getopt
import numpy as np

from genetic_algorithm.genetic_algorithm import GA


def print_usage():
    print("AlgoritmoGenetico usage:\n\npython algoritmo-genetico -p <popsize> -m <mutation-rate>")


def parse_opts(opts):
    popsize = None
    mutation_rate = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print_usage()
            exit()
        elif opts[i][0] == "-p":
            popsize = int(opts[i][1])
            if popsize % 2 != 0:
                print("Error!")
                print("Population must be even size!")
                exit()
        elif opts[i][0] == "-m":
            mutation_rate = float(opts[i][1][1:])

    if not (popsize and mutation_rate):
        print("Bad usage!")
        print_usage()
        exit()

    return popsize, mutation_rate


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hp:m:", ["m="])
    popsize, mutation_rate = parse_opts(opts)

    algoritmo = GA(popsize, mutation_rate)

    algoritmo.run()
