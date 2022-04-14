import numpy as np
import random
import math
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
        
# TODO add support for one-sigma
class OneFifth(Mutation):
    """ 1/5 success rule method.
    """
    def __init__(self, alt=False):
        if alt:
            self.mutate = self.mutate_alt

    def mutate(self, population: Population, gen_succ: int, gen_tot: int):
        c = 0.95
        k = 40  # sigmas reset patience
        # reset sigmas
        if gen_tot % k == 0:
            population.init_sigmas()
        # increare sigmas (explore more)
        elif gen_succ/gen_tot > 0.20:
            population.sigmas /= c
        # decrease sigmas (exploit more)
        elif gen_succ/gen_tot < 0.20:
            population.sigmas *= c
        # mutate components
        variations = np.random.normal(0, population.sigmas)
        population.individuals += variations


class Correlated(Mutation):
    """ Coorelated mutation
    """
    def mutate(self, population: Population, *_):
        lr = 1/np.sqrt(2*(np.sqrt(population.ind_size)))
        lr_prime = 1/(np.sqrt(2*population.ind_size))
        beta = math.pi/360  # was 36 and i changed it
        normal_matr_prime = np.random.normal(0,lr_prime,1)

        for ind_idx in range(population.pop_size):
            for sigma in range(population.ind_size):

                # Update our sigmas
                normal_matr = np.random.normal(0,lr,1)
                population.sigmas[ind_idx][sigma] = population.sigmas[ind_idx][sigma]*(
                            np.exp(normal_matr+normal_matr_prime))

                # Update angles
                alphas_noise = np.random.normal(0,beta,len(population.alphas[ind_idx]))
                population.alphas[ind_idx] = population.alphas[ind_idx] + alphas_noise

                # Out of boundary correction
                population.alphas[ind_idx][population.alphas[ind_idx] > math.pi] = population.alphas[ind_idx][population.alphas[ind_idx] > math.pi] - 2*math.pi*np.sign(population.alphas[ind_idx][population.alphas[ind_idx] > math.pi])

                #Calculate C matrix
                count = 0
                C = np.identity(population.ind_size)
                for i in range(population.ind_size-1):
                    for j in range(i+1,population.ind_size):
                        R = np.identity(population.ind_size)
                        R[i,i] = math.cos(population.alphas[ind_idx][count])
                        R[j,j] = math.cos(population.alphas[ind_idx][count])
                        R[i,j] = -math.sin(population.alphas[ind_idx][count])
                        R[j,i] = math.sin(population.alphas[ind_idx][count])
                        C = np.dot(C, R)
                        count += 1
                s = np.identity(population.ind_size)
                np.fill_diagonal(s, population.sigmas[ind_idx])
                C = np.dot(C, s)

                # Update offspring
                sigma_std = np.random.multivariate_normal(mean=np.full((population.ind_size),fill_value=0), cov=C)
                fix = np.array([ random.gauss(0,i) for i in sigma_std ])
                population.individuals[ind_idx] =  population.individuals[ind_idx] + fix
