import numpy as np
from classes.Population import *


class Mutation:
    def mutate(self):
        """ Mutate the population.
        """
        pass

    def __call__(self, *args):
        self.mutate(*args)


class IndividualSigma(Mutation):
    """ Individual sigma method.
    """
    def mutate(self, population: Population):
        # define tau and tau'
        tau = 1/np.sqrt(2*(np.sqrt(population.ind_size)))
        tau_prime = 1/(np.sqrt(2*population.ind_size))
        # create N and N' matrixes
        normal_matr_prime = np.random.normal(0,tau_prime,(population.pop_size,1))
        normal_matr = np.random.normal(0,tau,(population.pop_size, population.ind_size))
        #update our sigmas
        population.sigmas = population.sigmas * np.exp(normal_matr + normal_matr_prime)
        # update our individuals
        noises = np.random.normal(0,population.sigmas)
        population.individuals += noises
        
# TODO: complete algorithm
class Correlated(Mutation):
    def mutate(self, population: Population, minimize=True):
        # sort our values
        if minimize:
            sorted_ind = np.argsort(population.fitnesses)
        else:  # we need to reverse our indexes
            sorted_ind = np.argsort(population.fitnesses)[::-1]

        pass


class OneFifth(Mutation):
    """ One Fifth Rule
    """
    def mutate(self, population: Population):
        
        m = np.full(population.pop_size,fill_value=0.)
        C = np.identity(population.pop_size)
        mutation = np.random.multivariate_normal(mean=m, 
                                                cov=C,
                                                size=(population.pop_size,population.ind_size)
                                                 ).reshape((population.pop_size, population.ind_size))
        population.individuals += mutation


class OneFifth_(Mutation):

    def mutate(self, population: Population, better_gens, tot_gen):
        c = 0.95
        k = 50  # sigmas reset patience
        # reset sigmas
        if tot_gen % k == 0:
            population.sigma_init()
        # increare sigmas (explore more)
        if better_gens/tot_gen > 0.20:
            population.sigmas /= c
        # decrease sigmas (exploit more)
        elif better_gens/tot_gen < 0.20:
            population.sigmas *= c
        # mutate components
        variations = np.random.normal(0, population.sigmas)
        population.individuals += variations


