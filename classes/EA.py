from classes.Population import *
import numpy as np
import time


class EA:
    """ Main Evolutionary Strategy class
    """
    def __init__(self, minimize, budget,
                parents_size, offspring_size,
                individual_size,
                recombination, mutation, 
                selection, evaluation,
                verbose):
        self.minimize = minimize
        self.budget = budget
        self.parents_size = parents_size
        self.offspring_size = offspring_size
        self.individual_size = individual_size
        self.recombination = recombination
        self.mutation = mutation
        self.selection = selection
        self.evaluation = evaluation
        self.verbose=verbose
        self.parents = Population(  self.parents_size,
                                    self.individual_size,
                                    mutation)
        self.offspring = Population(self.offspring_size, 
                                    self.individual_size, 
                                    mutation)

    def run(self):
        """ Main function to run the Evolutionary Strategy
        """
        # Initialize budget
        curr_budget = 0
        best_budget = 0
        # initialize best evaluation as worst possible value
        best_eval = np.inf if self.minimize else np.NINF


        # Initial parents evaluation step
        self.parents.evaluate(self.evaluation)
        best_eval, best_index = self.parents.best_fitness(self.minimize)
        best_indiv = self.parents.individuals[best_index]
        curr_budget += self.parents_size

        while curr_budget < self.budget:

            # Recombination: creates new offspring
            if self.recombination is not None:
                self.recombination(self.parents, self.offspring)
            
            # Mutation: mutate individuals (offspring)
            self.mutation(self.offspring)

            # Evaluate offspring population
            self.offspring.evaluate(self.evaluation)
            curr_budget += self.offspring_size

            # Next generation parents selection
            self.selection(self.parents, self.offspring)

            # Evaluate new parent population
            self.parents.evaluate(self.evaluation)
            curr_budget += self.parents_size

            # Update the best individual in case of success
            curr_best_eval, curr_best_index = self.parents.best_fitness(self.minimize)
            current_best_indiv = self.parents.individuals[curr_best_index]
            success = False
            if self.minimize:
                if curr_best_eval < best_eval:
                    success = True
            else:
                if curr_best_eval > best_eval:
                    success = True
            if success:
                best_indiv = current_best_indiv
                best_eval = curr_best_eval
                best_budget = curr_budget

        return best_indiv, best_eval, best_budget