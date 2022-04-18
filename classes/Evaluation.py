import numpy as np


class Evaluate:
    def __call__(self):
        pass


class Ackley(Evaluate):
    """ Evaluate a solution on Ackley problem
        Minimization problem. Optimum is 0.
    """
    def __init__(self, a = 20, b = 0.2, c = 2*np.pi, minimize=True):
        self.a = a
        self.b = b
        self.c = c
        self.optimum = 0
        
    def __call__(self, x):
        ret_vals = []
        for ind_idx in range(x.shape[0]):
            dim = x.shape[1]
            term1 = -1. * self.a * np.exp(-1. * self.b * np.sqrt((1./dim) * sum(map(lambda i: i**2, x[ind_idx]))))
            term2 = -1. * np.exp((1./dim) * (sum(map(lambda j: np.cos(self.c * j), x[ind_idx]))))
            y = term1 + term2 + self.a + np.exp(1)
            ret_vals.append(y)
        return np.array(ret_vals)


class Rastrigin(Evaluate):
    """ Evaluate a solution on Rastringin problem.
        Minimization problem. Optimum is 0.
    """
    def __init__(self, a = 10, minimize=True):
        self.a = a
        self.optimum = 0
        
    def __call__(self, x):
        ret_vals = []
        for ind_idx in range(x.shape[0]):
            y = self.a * x.shape[1] + sum(map(lambda i: i**2 - self.a * np.cos(2*np.pi*i), x[ind_idx]))
            ret_vals.append(y)
        return np.array(ret_vals)