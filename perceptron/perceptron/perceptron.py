import numpy as np
import warnings
warnings.filterwarnings("ignore")


class IrisPerceptron(object):
    def __init__(self) -> None:
        super().__init__()

        self.n_classes = 3
        self.weigths = None
        self.bias = None

    def array_biggest_value(self, y):
        if y[0] > y [1] and y[0] > y[2]:
            return np.array([1, 0, 0]).reshape(3,1)
        if y[1] > y[0] and y[1] > y[2]:
            return np.array([0, 1, 0]).reshape(3,1)
        if y[2] > y[0] and y[2] > y[1]:
            return np.array([0, 0, 1]).reshape(3,1)
        # no caso de todos os valores serem iguais
        return y

    def train(self, max_it, learning_rate, X, d, activation_func, y_as_biggest_value=False) -> None:
        n_lines, n_features = X.shape

        self.weigths = np.zeros((self.n_classes, n_features))
        self.bias = np.zeros((self.n_classes, 1))

        epoch = 0
        err = 1.

        while epoch < max_it and err > 0.:
            #print(f'Training(epoch: {epoch} | error: {err} | bias: {self.bias.T})')
            err = 0.

            for i in range(n_lines):
                y = activation_func(
                    np.matmul(self.weigths, X[i].reshape((n_features, 1))) + self.bias)

                # computando a classe para saída que apresentar o maior valor.
                if y_as_biggest_value:
                    y = self.array_biggest_value(y)

                e = d[i].reshape((self.n_classes, 1)) - y

                self.weigths = self.weigths + \
                    learning_rate * \
                    np.matmul(e, X[i].reshape((n_features, 1)).T)
                self.bias = self.bias + learning_rate * e

                err = err + np.sum(np.power(e, 2))

            epoch = epoch + 1

    def test(self, X, d, activation_func, y_as_biggest_value=False) -> None:
        n_lines, n_features = X.shape

        correct = 0
        for i in range(n_lines):
            y = activation_func(
                np.matmul(self.weigths, X[i].reshape((n_features, 1))) + self.bias)

            # computando a classe para saída que apresentar o maior valor.
            if y_as_biggest_value: 
                y = self.array_biggest_value(y)

            e = d[i].reshape((self.n_classes, 1)) - y

            if np.nonzero(e)[0].size == 0:
                correct = correct + 1

        return correct, (correct / n_lines) * 100
