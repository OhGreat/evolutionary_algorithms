from classes.Population import *
import numpy as np
import random


class Recombination:
    def __call__(self):
        pass


class Intermediate(Recombination):
    """ Creates offspring by taking the average values of the parents
    """
    def __call__(self, parents: Population, offspring: Population):
        # range of parent indexes to sample from 
        idxes = range(parents.pop_size)
        # range of number of offsprings to create
        offspring_rng = range(offspring.pop_size)
        for i in offspring_rng:
            # pick two parents at random
            p1, p2 = random.sample(idxes, k=2)
            # update offspring population
            offspring.individuals[i] = (parents.individuals[p1] + parents.individuals[p2]) / 2
            offspring.sigmas[i] = (parents.sigmas[p1] + parents.sigmas[p2]) / 2
            # recombine alphas if we are using them
            if parents.mutation.__class__.__name__ == "Correlated":
                offspring.alphas[i] = (parents.alphas[p1] + parents.alphas[p2]) / 2
