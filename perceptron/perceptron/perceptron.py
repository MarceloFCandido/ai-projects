import numpy as np


class IrisPerceptron(object):
    def __init__(self) -> None:
        super().__init__()

        self.n_classes = 3
        self.weigths = None
        self.bias = None

    def train(self, max_it, learning_rate, X, d, activation_func) -> None:
        n_lines, n_features = X.shape

        self.weigths = np.zeros((self.n_classes, n_features))
        self.bias = np.zeros((self.n_classes, 1))

        epoch = 0
        err = 1.

        while epoch < max_it and err > 0.:
            print(f'Training(epoch: {epoch} | error: {err} | bias: {self.bias.T})')
            err = 0.

            for i in range(n_lines):
                y = activation_func(
                    np.matmul(self.weigths, X[i].reshape((n_features, 1))) + self.bias)

                e = d[i].reshape((self.n_classes, 1)) - y

                self.weigths = self.weigths + \
                    learning_rate * \
                    np.matmul(e, X[i].reshape((n_features, 1)).T)
                self.bias = self.bias + learning_rate * e

                err = err + np.sum(np.power(e, 2))

            epoch = epoch + 1

    def test(self, X, d, activation_func) -> None:
        n_lines, n_features = X.shape

        correct = 0
        for i in range(n_lines):
            y = activation_func(
                np.matmul(self.weigths, X[i].reshape((n_features, 1))) + self.bias)
            e = d[i].reshape((self.n_classes, 1)) - y

            if np.nonzero(e)[0].size == 0:
                correct = correct + 1

        return correct, (correct / n_lines) * 100
