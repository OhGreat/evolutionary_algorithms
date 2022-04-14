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
        offspring.individuals = []
        offspring.sigmas = []
        for _ in range(offspring.pop_size):
            # get pair
            i1, i2 = random.sample(range(parents.individuals.shape[0]), k=2)
            x1, x2 = parents.individuals[i1], parents.individuals[i2]
            s1, s2 = parents.sigmas[i1], parents.sigmas[i2]
            # recombinate components and sigmas
            offspring.individuals.append(np.array([(x1_i + x2_i) / 2 for x1_i, x2_i in zip(x1, x2)]))
            if not parents.mutation.__class__.__name__ == "OneSigma":
                # select the sigma of each component as the mean of the sigmas of the two components
                offspring.sigmas.append(np.array([(s1_i + s2_i) / 2 for s1_i, s2_i in zip(s1, s2)]))
            else:
                # sigma is the mean of the two sigmas
                offspring.sigmas.append((s1 + s2) / 2)
        offspring.individuals = np.vstack(offspring.individuals)
        if not parents.mutation.__class__.__name__ == "OneSigma":
            offspring.sigmas = np.vstack(offspring.sigmas)
        elif parents.mutation.__class__.__name__ == "Correlated":
            offspring.sigmas = np.vstack(offspring.sigmas)
            offspring.alphas = np.vstack(offspring.alphas)
        else:
            offspring.sigmas = np.array(offspring.sigmas)

class IntermediateD(Recombination):
    """ Creates offspring by taking the average values of the parents
    """

    def __call__(self, parents: Population, offspring: Population):
        idxes = range(0,parents.pop_size)
        
        rng = range(parents.pop_size)
        for i in rng:
            # Pick two parents at random
            p1, p2 = random.sample(idxes, k=2)

            # Create offspring 
            offspring.individuals[i] = (parents.individuals[p1] + parents.individuals[p2]) / 2
            offspring.sigmas[i] = (parents.sigmas[p1] + parents.sigmas[p2]) / 2

            if parents.mutation.__class__.__name__ == "Correlated":
                offspring.alphas[i] = (parents.alphas[p1] + parents.alphas[p2]) / 2
