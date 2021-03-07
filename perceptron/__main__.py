from os import device_encoding
import sys
from getopt import getopt
import numpy as np

from perceptron.perceptron import IrisPerceptron


def print_usage():
    print("Perceptron usage:\n\npython perceptron -l <learning-rate> -i <max-iterations> --data-file <data-file>")


def parse_opts(opts):
    learning_rate = None
    max_iterations = None
    data_file = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print_usage()
            exit()
        elif opts[i][0] == "-l":
            learning_rate = float(opts[i][1][1:])
        elif opts[i][0] == "-i":
            max_iterations = int(opts[i][1])
        elif opts[i][0] == "--data-file":
            data_file = opts[i][1]

    if not (learning_rate and max_iterations and data_file):
        print("Bad usage!")
        print_usage()
        exit()

    return learning_rate, max_iterations, data_file


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hl:i:", ["data-file="])
    learning_rate, max_iterations, data_file = parse_opts(opts)

    data = np.genfromtxt(data_file, delimiter=',',
                         dtype=float, usecols=(0, 1, 2, 3))

    def map_classifications(x):
        if x == 'Iris-setosa':
            return np.array([1, 0, 0])
        elif x == 'Iris-versicolor':
            return np.array([0, 1, 0])
        elif x == 'Iris-virginica':
            return np.array([0, 0, 1])

    classifications = np.array([map_classifications(x) for x in np.genfromtxt(
        data_file, delimiter=',', dtype=str, usecols=(4))], dtype=int)

    # shuffling input arrays
    p = np.random.permutation(data.shape[0])
    X = data[p]
    d = classifications[p]

    perceptron = IrisPerceptron()
    # np.heaviside eh a funcao degrau
    perceptron.train(max_iterations, learning_rate, X[:100],
                     d[:100], lambda x: np.heaviside(x, 1))
    print(perceptron.test(X[100:], d[100:], lambda x: np.heaviside(x, 1)))
