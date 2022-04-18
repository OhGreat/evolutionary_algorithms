from cmath import inf
import numpy as np
from classes.Population import *


class Selection:
    def __call__(self):
        pass


class PlusSelection(Selection):
    """ Get the best individuals from both the parent and offspring populations
    """
    def __call__(self, parents: Population, offspring: Population, minimize=True):
        fitnesses_stacked = np.hstack([parents.fitnesses, offspring.fitnesses])
        # get sorted indexes
        if minimize:
            sorted_ind = np.argsort(fitnesses_stacked)[:parents.pop_size]
        else: 
            sorted_ind = np.argsort(fitnesses_stacked)[::-1][:parents.pop_size]
        # update parent population
        parents.individuals = np.vstack([parents.individuals, offspring.individuals])[sorted_ind]
        parents.sigmas = np.vstack([parents.sigmas, offspring.sigmas])[sorted_ind]
        parents.fitnesses = fitnesses_stacked[sorted_ind] 
        if parents.mutation.__class__.__name__ == "Correlated":
                parents.alphas = np.vstack([parents.alphas, offspring.alphas])[sorted_ind]


class CommaSelection(Selection):
    """ Get the best individuals only from the offspring population
    """
    def __call__(self, parents: Population, offspring: Population, minimize=True):
        # get sorted indexes
        if minimize:
            sorted_ind = np.argsort(offspring.fitnesses)[:parents.pop_size]
        else:  # we need to reverse our indexes
            sorted_ind = np.argsort(offspring.fitnesses)[::-1][:parents.pop_size]
        # update parent population
        parents.individuals = offspring.individuals[sorted_ind]
        parents.sigmas = offspring.sigmas[sorted_ind]
        parents.fitnesses = offspring.fitnesses[sorted_ind] 
        if parents.mutation.__class__.__name__ == "Correlated":
                parents.alphas = offspring.alphas[sorted_ind]

class OneFifthSelection(Selection):
    """ Selection for 1/5 success rule
    """
    def __call__(self, parents : Population, offspring : Population, minimize=True):
        decrease_multiplier = 0.9 #(1.5)**(-1/4)
        increase_multiplier = 1.5

        #print(np.max(parents.sigmas), np.min(parents.sigmas))
        if parents.sigmas.max() > 1e-5 or parents.sigmas.min() < 1e-5:
                parents.step_size = 1.8
                parents.sigma_init()

        # sigma update
        if minimize:
            if parents.fitnesses[0] > offspring.fitnesses[0]:
                # new best found
                parents.individuals = offspring.individuals
                parents.sigmas *= increase_multiplier
            else:  # better solution not found
                parents.sigmas *= decrease_multiplier 

        else: # maximization problem
            if parents.fitnesses[0] < offspring.fitnesses[0]:
                # new best found
                parents.individuals = offspring.individuals
                parents.sigmas *= increase_multiplier
            else: # better solution not found
                parents.sigmas *= decrease_multiplier

        # step size update
        """if minimize:
            if parents.fitnesses[0] >= offspring.fitnesses[0]:
                # new best found
                parents.individuals = offspring.individuals
                parents.step_size *= increase_multiplier
            else:  # better solution not found
                parents.step_size *= decrease_multiplier 
        else: # maximization problem
            if parents.fitnesses[0] <= offspring.fitnesses[0]:
                # new best found
                parents.individuals = offspring.individuals
                parents.step_size *= increase_multiplier
            else: # better solution not found
                parents.step_size *= decrease_multiplier"""

