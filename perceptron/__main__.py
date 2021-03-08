from os import device_encoding
import sys
from getopt import getopt
import numpy as np
import matplotlib.pyplot as plt 

from perceptron.perceptron import IrisPerceptron


def print_usage():
    print("Perceptron usage:\n\npython perceptron -l <learning-rate> -i <max-iterations> --data-file <data-file>")


def parse_opts(opts):
    learning_rate = None
    max_iterations = None
    data_file = None
    with_graphs = None

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

def plot_graphs(max_iterations, learning_rate, X, d):
    # Rodando com variacao de parametros para comparacao

    learning_arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    learning_data_degrau = []
    learning_data_sigmoid= []

    for l in learning_arr:
        print(f"Learning rate: {l}")

        perceptron = IrisPerceptron()
        error = perceptron.train(max_iterations, l, X[:100], d[:100], lambda x: np.heaviside(x, 1))
        result = perceptron.test(X[100:], d[100:], lambda x: np.heaviside(x, 1))
        # print(f" Função degrau\n Número de acertos: {result[0]}\tAcurácia: {round(result[1], 2)}%\n")

        learning_data_degrau.append(round(result[1], 2))

        perceptron = IrisPerceptron()
        perceptron.train(max_iterations, l, X[:100], d[:100], lambda x: 1/(1 + np.exp(-x)), True)
        result = perceptron.test(X[100:], d[100:], lambda x: 1/(1 + np.exp(-x)), True)
        # print(f" Função sigmoidal\n Número de acertos: {result[0]}\tAcurácia: {round(result[1], 2)}%\n")

        learning_data_sigmoid.append(round(result[1], 2))

    max_it_arr = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350]
    max_it_data_degrau = []
    max_it_data_sigmoid= []

    for m in max_it_arr:
        print(f"Máximo de iterações: {m}")

        perceptron = IrisPerceptron()
        error = perceptron.train(m, learning_rate, X[:100], d[:100], lambda x: np.heaviside(x, 1))
        result = perceptron.test(X[100:], d[100:], lambda x: np.heaviside(x, 1))
        # print(f" Função degrau\n Número de acertos: {result[0]}\tAcurácia: {round(result[1], 2)}%\n")

        max_it_data_degrau.append(round(result[1], 2))

        perceptron = IrisPerceptron()
        perceptron.train(m, learning_rate, X[:100], d[:100], lambda x: 1/(1 + np.exp(-x)), True)
        result = perceptron.test(X[100:], d[100:], lambda x: 1/(1 + np.exp(-x)), True)
        # print(f" Função sigmoidal\n Número de acertos: {result[0]}\tAcurácia: {round(result[1], 2)}%\n")

        max_it_data_sigmoid.append(round(result[1], 2))

    # print(learning_data_degrau, learning_data_sigmoid)

    x1 = learning_arr
    y1 = learning_data_degrau

    x2 = learning_arr
    y2 = learning_data_sigmoid

    # print(max_it_data_degrau, max_it_data_sigmoid)

    x3 = max_it_arr
    y3 = max_it_data_degrau

    x4 = max_it_arr
    y4 = max_it_data_sigmoid

    fig, axs = plt.subplots(2)
    axs[0].plot(x1, y1, label = "Função degrau")
    axs[0].plot(x2, y2, label = "Função sigmoidal")
    axs[0].set(xlabel = 'Learning rate', ylabel = 'Acurácia') 
    axs[0].set_title("Acurácia x Learning rate")
    axs[0].legend()

    axs[1].plot(x3, y3, label = "Função degrau")
    axs[1].plot(x4, y4, label = "Função sigmoidal")
    axs[1].set(xlabel = 'Máximo de iterações', ylabel ='Acurácia')
    axs[1].set_title("Acurácia x Máximo de iterações")
    axs[1].legend()
    
    plt.show()


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

    print("** Função degrau **")
    perceptron = IrisPerceptron()
    perceptron.train(max_iterations, learning_rate, X[:100], d[:100], lambda x: np.heaviside(x, 1))
    result = perceptron.test(X[100:], d[100:], lambda x: np.heaviside(x, 1))
    print(f" Número de acertos: {result[0]}\n", f"Acurácia: {round(result[1], 2)}%\n")

    print("\n** Função sigmoidal **")
    perceptron = IrisPerceptron()
    perceptron.train(max_iterations, learning_rate, X[:100], d[:100], lambda x: 1/(1 + np.exp(-x)), True)
    result = perceptron.test(X[100:], d[100:], lambda x: 1/(1 + np.exp(-x)), True)
    print(f" Número de acertos: {result[0]}\n", f"Acurácia: {round(result[1], 2)}%\n")

    plot_graphs(max_iterations, learning_rate, X, d)
