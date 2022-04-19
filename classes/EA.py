from classes.Population import *
import numpy as np


class EA:
    """ Main Evolutionary Strategy class
    """
    def __init__(self, minimize, budget, patience,
                parents_size, offspring_size,
                individual_size,
                recombination, mutation, 
                selection, evaluation,
                verbose):
        self.minimize = minimize
        self.budget = budget
        self.patience = patience
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
        """ Runs the Evolutionary Strategy.
            Returns the best individual and the best fitness.
        """
        # Initialize budget and patience
        self.curr_budget, self.curr_patience = 0, 0
        # Initialize number of better generations found total generations
        self.better_generations = 0
        self.total_generations = 1
        # Initial parents setup
        self.parents.evaluate(self.evaluation)
        self.best_eval, self.best_index = self.parents.best_fitness(self.minimize)
        self.best_indiv = self.parents.individuals[self.best_index]
        self.curr_budget += self.parents_size

        while self.curr_budget < self.budget:
            # Recombination: creates new offspring
            if self.recombination is not None:
                self.recombination(self.parents, self.offspring)
            # Mutation: mutate offspring population
            self.mutation(self.offspring)
            # Evaluation: evaluate offspring population
            self.offspring.evaluate(self.evaluation)
            # Selection: select the parents for the next geneation
            self.selection(self.parents, self.offspring, self.minimize)
            # Update control variables, e.g. budget and best individual
            self.update_control_vars()
        return self.best_indiv, self.best_eval

    def update_control_vars(self):
        """ Updates all control variables
        """
        # Update the best individual
        curr_best_eval = self.parents.fitnesses[0]
        new_best_found = False
        if self.minimize and curr_best_eval < self.best_eval:
            new_best_found = True
        elif curr_best_eval > self.best_eval:
            new_best_found = True
        if new_best_found:
            self.best_indiv = self.parents.individuals[0]
            self.best_eval = curr_best_eval
            # increment number of successful generations
            self.better_generations += 1
            # reset patience since we found a new best
            self.curr_patience = 0
            # debug print
            if self.verbose > 1:
                print(f"New best: {self.best_eval}, budget: {self.curr_budget}")
        else:  # new best not found, increment current patience counter
            self.curr_patience += 1
        # increment past generations counter
        self.total_generations += 1

        # update next generation success probability
        self.offspring.success_prob = self.better_generations / self.total_generations

        # reset sigmas if patience has been defined
        if self.patience:
            if self.parents.mutation.__class__.__name__ == "OneFifth":
                # we reset every specified interval
                if self.total_generations + 1 % self.patience == 0:
                    self.parents.sigma_init()
            else:  # we reset sigmas when patience expires
                if self.curr_patience >= self.patience:
                    self.parents.sigma_init()
                    self.curr_patience = 0
        
        # increment current budget
        self.curr_budget += self.offspring_size
