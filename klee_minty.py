import numpy as np


class KleeMintyCube:
    def __init__(self, n):
        self.n = n
        self.objective_coefs = np.array([10 ** (n - (j + 1)) for j in range(n)])
        self.constraints_coefs = np.zeros((n, n))
        for i in range(n):
            for j in range(i):
                self.constraints_coefs[i][j] = 2 * 10 ** (i - j)
            self.constraints_coefs[i][i] = 1
        self.constraints_boundaries = np.array([100 ** i for i in range(n)])

    def objective(self, X):
        return X.dot(self.objective_coefs)

    def constraints(self, X):
        return X.dot(self.constraints_coefs) - self.constraints_boundaries

    def constraint(self, X, i):
        return X.dot(self.constraints_coefs[i]) - self.constraints_boundaries[i]
