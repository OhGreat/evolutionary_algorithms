from math import sqrt
from typing import Tuple
from numpy import exp
from numpy.random import normal, uniform
import numpy as np

from EA_multiproc.Pop_multiproc import Individual, Population_multiproc


class Mutation_multiproc:
    """ Template class
    """
    def __call__(self, pop: Individual) -> None:
        """ Inplace mutation on population should be defined here.
        """
        pass

    def set_mut_params(self, pop: Individual) -> None:
        """ Should set the mutation parameters on the individuals
        of the population if required.
        """
        pass


class IndividualSigma_multiproc(Mutation_multiproc):
    """ Sigmas for each individual in the population.
    """
    def __call__(self, individual: Individual) -> Tuple[np.array, np.array]:
        # define tau and tau' learning rates
        tau = 1/sqrt(2*(sqrt(individual.size)))
        tau_prime = 1/(sqrt(2*individual.size))
        # create N and N' matrixes
        normal_matr = normal(0,tau,individual.size)
        normal_matr_prime = normal(0,tau_prime,1)
        #update our sigmas
        mut_params = individual.mut_params * exp(normal_matr + normal_matr_prime)
        # update our individuals
        if (mut_params < 0).any(): # make sure sigmas are positive
            mut_params = self.get_init_params()
        # create noise and update population
        noises = normal(0,mut_params)
        individual.values += noises

        return individual.values, mut_params

    def set_mut_params(self, pop: Population_multiproc) -> None:
        """ Sets the mutation parameters to the population.
        """
        for ind in pop.individuals:
            ind.mut_params = np.random.uniform(
                max(0, np.min(ind.values)/6),
                np.max(ind.values)/6,
                size=ind.size
            )
        pop.has_mut_params = True


class BitFlip_multiproc(Mutation_multiproc):
    """ Multiprocessing binary mutation consisting of bit flips with probability p.
    """
    def __init__(self, p):
        self.p = 1 - p

    def __call__(self, ind: Individual) -> np.array:
        return np.array([not gene if uniform() > self.p else gene 
                                            for gene in ind.values]), None


class RandomChoice(Mutation_multiproc):
    """ Randomly flip the values of the individual between an interval.
    """
    def __init__(self, choices) -> None:
        super().__init__()

    def __call__(self, pop: Population_multiproc) -> None:
        pass