from EA_components_OhGreat.Population_torch import Population_torch
from EA_components_OhGreat.Recombination import Recombination
import torch
import numpy as np

class GlobalDiscrete_torch(Recombination):
    """ Creates discrete recombined offsprings.
    """
    def __init__(self, device):
        self.device = device

    def __call__(self, parents: Population_torch, offspring: Population_torch):
        # rng
        parent_choices = torch.randint(0,parents.pop_size, 
                            size=(offspring.pop_size, offspring.ind_size), 
                            device=self.device)
        # print(parent_choices.shape)
        # exit()
        # reset offspring
        offspring.individuals = []
        offspring.sigmas = []
        for i in range(offspring.pop_size):
            # create new offspring
            offspring.individuals.append([curr_par[curr_choice] 
                                            for curr_par, curr_choice in 
                                            zip(parents.individuals.T, 
                                                parent_choices[i])])
            # create offspring's sigmas
            offspring.sigmas.append([curr_par[curr_choice] 
                                            for curr_par, curr_choice in 
                                            zip(parents.sigmas.T, 
                                                parent_choices[i])])
        # revert arrays to numpy
        offspring.individuals = torch.tensor(offspring.individuals, device=self.device)
        offspring.sigmas = torch.tensor(offspring.sigmas, device=self.device)