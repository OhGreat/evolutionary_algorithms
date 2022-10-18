import torch
import numpy as np
from torch.distributions import Normal
from EA_components_OhGreat.Population import Population
from EA_components_OhGreat.Mutation import Mutation

class IndividualSigma_torch(Mutation):
    """ Individual sigma method.
    """
    def __init__(self, device):
        self.device = device
        self.tau = torch.tensor([0.])
        self.tau_prime = torch.tensor([0.])

    def mutate(self, population: Population):
        # define tau and tau'
        tau = 1/torch.sqrt(2*(torch.sqrt(population.ind_size))).squeeze()
        tau_prime = 1/torch.sqrt(2*population.ind_size)
        # create N and N' matrixes
        normal_matr = Normal(0,tau).sample((population.pop_size, population.ind_size))
        normal_matr_prime = Normal(0,tau_prime).sample((population.pop_size))
        # print(normal_matr.shape, normal_matr_prime.shape)
        # exit()
        #update our sigmas
        population.sigmas = population.sigmas * torch.exp(normal_matr+normal_matr_prime)
        # update our individuals
        if (population.sigmas < 0).any(): # make sure sigmas are positive
            print("Sigmas < 0! Trying a reset..", population.sigmas)
            population.sigma_init()
        # create noise and update population
        try:
            noises = Normal(0,population.sigmas).sample()
        except:
            print("fuck")
            population.sigma_init()
            noises = Normal(0,population.sigmas).sample()
        
        population.individuals += noises