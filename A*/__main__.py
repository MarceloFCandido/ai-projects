import sys
from getopt import getopt
import numpy as np

from a_star.a_star import A_Star


def print_usage():
    print("A* usage:\n\npython A* -s <souce-station> -d <destiny-station> --heuristics=<heuristics-file> --real_distances=<distances-file>")


def parse_opts(opts):
    objective = [-1, -1]
    heuristics_file = ""
    distances_file = ""

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print_usage()
            exit()
        elif opts[i][0] == "-s":
            objective[0] = int(opts[i][1][1:]) - 1
        elif opts[i][0] == "-d":
            objective[1] = int(opts[i][1][1:]) - 1
        elif opts[i][0] == "--heuristics":
            heuristics_file = opts[i][1]
        elif opts[i][0] == "--real_distances":
            distances_file = opts[i][1]

    if not (sum(objective) != -2 and heuristics_file and distances_file):
        print("Bad usage\n")
        print_usage()
        exit()

    return tuple(objective), heuristics_file, distances_file


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hs:d:", [
                        "heuristics=", "real_distances="])
    objective, heuristics_filename, distances_filename = parse_opts(opts)

    a_star = A_Star(objective, heuristics_filename, distances_filename)

    a_star = A_Star(objective, heuristics_file, distances_file)
    a_star.run()
