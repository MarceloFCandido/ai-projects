import numpy as np


class Perceptron(object):
    def __init__(self) -> None:
        super().__init__(self)

        self.w = None
        self.e = None

    def train(self, max_it, learning_rate, X, d, activation_func) -> None:
        N = X.shape[0]

        b = 0.
        self.w = np.zeros(N)

        y = np.zeros(N)
        self.e = np.zeros(N)

        epoch = 0
        err = 1.

        while epoch < max_it and err > 0.:
            print(f'Training(Epoch: {epoch} | error: {err} | bias: {b})')
            err = 0.

            for i in range(N):
                y[i] = activation_func(self.w[i] * X[i] + b)
                self.e[i] = d[i] - y[i]
                self.w[i] = self.w[i] + learning_rate * self.e[i] * X[i]

                b = b + learning_rate * self.e[i]
                err = err + self.e[i] * self.e[i]

            epoch = epoch + 1

    def test() -> None:
        pass
