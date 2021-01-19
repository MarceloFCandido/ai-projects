import sys
from getopt import getopt
import numpy as np


def parse(opts):
    objective = ["", ""]

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print(
                "A* usage:\npython A* -s <souce-station> -d <destiny-station> --heuristics=<heuristics-file> --real_distances=<distances-file>")
            exit()
        elif opts[i][0] == "-s":
            objective[0] = opts[i][0]
        elif opts[i][0] == "-d":
            objective[1] = opts[i][0]


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hs:d:", [
                        "heuristics=", "real_distances="])
    objective, heuristics_file, distances_file = parse(opts)
