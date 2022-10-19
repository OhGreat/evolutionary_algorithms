import torch
import numpy as np
from math import sqrt
from torch.distributions import Normal
from EA_components_OhGreat.Population_torch import Population_torch


class IndividualSigma_torch():
    """ Individual sigma method.
    """
    def __init__(self, device):
        self.device = device
        self.tau = torch.tensor([0.]).to(device).resize_(0)
        self.tau_prime = torch.tensor([0.]).to(device).resize_(0)

    def mutate(self, population: Population_torch):
        # define tau and tau'
        torch.divide(1,torch.sqrt(2*(torch.sqrt(population.ind_size_v[0]))), out=self.tau)
        torch.divide(1,torch.sqrt(2*population.ind_size_v), out=self.tau_prime)
        # create N and N' matrixes
        normal_matr = Normal(0,self.tau).sample((population.pop_size, population.ind_size))
        normal_matr_prime = Normal(0,self.tau_prime).sample(population.pop_size_v)
        #update our sigmas
        population.sigmas = population.sigmas * torch.exp(normal_matr+normal_matr_prime)
        # update our individuals
        if (population.sigmas <= 0).any(): # make sure sigmas are positive
            population.sigma_init()
        # create noise and update population
        noises = Normal(0,population.sigmas).sample()
        
        population.individuals += noises


