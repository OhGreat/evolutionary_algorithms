import numpy as np
from numpy import exp
from numpy.random import normal
from math import sqrt
from EA_components_OhGreat.Population import *


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
        population.sigmas *= exp(normal_matr)
        if (population.sigmas < 0).any(): # make sure sigmas are positive
            population.sigma_init()
        # update individuals
        population.individuals += normal(0, population.sigmas)


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
        population.sigmas = population.sigmas * exp(normal_matr + normal_matr_prime)
        # update our individuals
        if (population.sigmas < 0).any(): # make sure sigmas are positive
            population.sigma_init()
        # create noise and update population
        noises = normal(0,population.sigmas)
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
        population.sigmas = population.sigmas * exp(normal_matr + normal_matr_prime)
        # update our individuals
        if (population.sigmas < 0).any(): # make sure sigmas are positive
            population.sigma_init()
        # create noise and update population
        noises = normal(0,population.sigmas)
        population.individuals += noises

        return population.individuals, population.sigmas
