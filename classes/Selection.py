import numpy as np
from classes.Population import *


class Selection:
    def __call__(self):
        pass


# TODO add maximization case (argsort)
class PlusSelection(Selection):
    """ Get the best individuals from both the parent and offspring populations
    """
    def __call__(self, parents: Population, offspring: Population, minimize=True):
        sorted_ind = np.argsort(np.hstack([parents.fitnesses, offspring.fitnesses]))
        parents.individuals = np.vstack([parents.individuals, offspring.individuals])[sorted_ind][:parents.pop_size]
        parents.sigmas = np.vstack([parents.sigmas, offspring.sigmas])[sorted_ind][:parents.pop_size]
        if parents.mutation.__class__.__name__ == "Correlated":
                parents.alphas = np.vstack([parents.alphas, offspring.alphas])[sorted_ind][:parents.pop_size]


# TODO add maximization case (argsort)
class CommaSelection(Selection):
    """ Get the best individuals only from the offspring population
    """
    def __call__(self, parents: Population, offspring: Population, minimize=True):
        sorted_ind = np.argsort(offspring.fitnesses)
        parents.individuals = offspring.individuals[sorted_ind][:parents.pop_size]
        parents.sigmas = offspring.sigmas[sorted_ind][:parents.pop_size]
        if parents.mutation.__class__.__name__ == "Correlated":
                parents.alphas = offspring.alphas[sorted_ind][:parents.pop_size]