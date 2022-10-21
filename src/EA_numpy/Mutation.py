import numpy as np
from numpy import exp
from numpy.random import normal
from math import sqrt
from EA_numpy.Population import *


class Mutation:
    def mutate(self):
        """ Mutate the population.
        """
        pass

    def __call__(self, *args):
        self.mutate(*args)


class OneSigma(Mutation):
    """ One Sigma method to control all population.
    """
    def mutate(self, population: Population):
        # define learning rate
        tau = 1/sqrt(population.ind_size)
        # create gaussian array to update sigmas
        normal_matr = normal(0, tau, size=(population.ind_size))
        # update sigmas
        population.mut_params *= exp(normal_matr)
        if (population.mut_params < 0).any(): # make sure sigmas are positive
            population.mut_params_init()
        # update individuals
        population.individuals += normal(0, population.mut_params)


class IndividualSigma(Mutation):
    """ Sigmas for each individual in the population.
    """
    def mutate(self, population: Population):
        # define tau and tau' learning rates
        tau = 1/sqrt(2*(sqrt(population.ind_size)))
        tau_prime = 1/(sqrt(2*population.ind_size))
        # create N and N' matrixes
        normal_matr = normal(0,tau,(population.pop_size, population.ind_size))
        normal_matr_prime = normal(0,tau_prime,(population.pop_size,1))
        #update our sigmas
        population.mut_params = population.mut_params * exp(normal_matr + normal_matr_prime)
        # update our individuals
        if (population.mut_params < 0).any(): # make sure sigmas are positive
            population.mut_params_init()
        # create noise and update population
        noises = normal(0,population.mut_params)
        population.individuals += noises


class IndividualSigma_multiprocess(Mutation):
    """ Sigmas for each individual in the population.
    """
    def mutate(self, population: Population):
        # define tau and tau' learning rates
        tau = 1/sqrt(2*(sqrt(population.ind_size)))
        tau_prime = 1/(sqrt(2*population.ind_size))
        # create N and N' matrixes
        normal_matr = normal(0,tau,(population.pop_size, population.ind_size))
        normal_matr_prime = normal(0,tau_prime,(population.pop_size,1))
        #update our sigmas
        population.mut_params = population.mut_params * exp(normal_matr + normal_matr_prime)
        # update our individuals
        if (population.mut_params < 0).any(): # make sure sigmas are positive
            population.mut_params_init()
        # create noise and update population
        noises = normal(0,population.mut_params)
        population.individuals += noises

        return population.individuals, population.mut_params
