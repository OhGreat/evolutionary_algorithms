import numpy as np
import multiprocessing
from math import floor
from typing import List, Tuple

from EA_multiproc.Pop_multiproc import Population_multiproc
from EA_multiproc.Rec_multiproc import Rec_multiproc
from EA_multiproc.Mut_multiproc import Mutation_multiproc
from EA_multiproc.Sel_multiproc import Selection


class EA_mixed:
    """ Main Evolutionary Strategy class
    """
    def __init__(
        self,
        minimize: int,
        budget: int,
        patience: int,
        parents_list: List[Population_multiproc],
        offspring_list: List[Population_multiproc],
        recombination: List[Rec_multiproc],
        mutation: List[Mutation_multiproc],
        selection: List[Selection],
        evaluation,
        pool_size: int,
        verbose: int,
    ) -> None:
        self.minimize = minimize
        self.budget = budget
        self.patience = patience
        self.parents_list = parents_list
        self.offspring_list = offspring_list
        self.recombination = recombination
        self.mutation = mutation
        self.selection = selection
        self.evaluation = evaluation
        self.pool_size = pool_size
        self.verbose=verbose

    def run(self) -> Tuple[np.array, np.array]:
        """ Runs the Evolutionary Strategy.
            Returns the best individual and the best fitness.
        """
        # Create processes pool
        pool = multiprocessing.Pool(floor(multiprocessing.cpu_count()/2)) if self.pool_size is None else multiprocessing.Pool(self.pool_size)
        if self.verbose > 1:
            print(f"Using {floor(multiprocessing.cpu_count()/2)} threads.")
        # Initialize budget and patience
        self.curr_budget, self.curr_patience = 0, 0
        # Initialize number of better generations found and total generations counters
        self.better_generations = 0
        self.gen_count = 0
        self.all_best_evals = []

        # TODO: fix evaluation with zip
        # Initial parents_list evaluation
        res = pool.map(func=self.evaluation, iterable=zip([pars.individuals for pars in self.parents_list ]))
        exit()
        self.parents_list.fitnesses = np.array(res)

        # TODO: fix
        # keep bests
        self.best_eval, self.best_index = self.parents_list.best_fitness(self.minimize)
        self.best_indiv = self.parents_list.individuals[self.best_index]
        self.curr_budget += self.parents_list.pop_size
        # debug print
        if self.verbose > 1: # prints zeneration 0 best eval
            print(
                f"Generation {self.gen_count} \
                Best eval: {np.round(self.best_eval, 3)}, \
                budget: {self.curr_budget}/{self.budget}"
            )

        # TODO: fix
        while self.curr_budget < self.budget:
            # check offspring_list population size to match maximum budget for last iteration
            if (self.budget - self.curr_budget) / self.offspring_list.pop_size < 1:
                self.resize_population()

            # Recombination
            if self.recombination is not None:
                # recombine discrete part
                for parents, offsprings, rec in zip(self.parents_list, self.offspring_list, self.recombination):
                    self.recombination.curr_parents_list = parents
                    res = pool.map(func=rec, iterable=offsprings.individuals)
                    for ind, new_vals in zip(parents.individuals, res):
                        ind.values = new_vals[0]
                        ind.mut_params = new_vals[1]
            
            # TODO: fix
            # Mutation
            # mutate discrete part
            res = pool.map_async(func=self.disc_mutation, iterable=self.disc_offspring_list.individuals).get()
            for ind, new_vals in zip(self.disc_offspring_list.individuals, res):
                ind.values = new_vals[0]
                ind.mut_params = new_vals[1]
            # mutate continuous part
            res = pool.map_async(func=self.cont_mutation, iterable=self.offspring_list.individuals).get()
            for ind, new_vals in zip(self.offspring_list.individuals, res):
                ind.values = new_vals[0]
                ind.mut_params = new_vals[1]

            # TODO: fix mixed evaluation (use zip on disc and cont)
            # Evaluation
            res = pool.map(func=self.evaluation, iterable=self.offspring_list.individuals)
            self.offspring_list.fitnesses = np.array(res)

            # Selection
            # TODO: selection for each group in population list
            # select discrete parts
            self.selection(self.disc_parents_list, self.disc_offspring_list, self.minimize)
            # select continuous part
            self.selection(self.parents_list, self.offspring_list, self.minimize)

            # Update control variables, e.g. budget and best individual
            self.update_control_vars()
        if self.verbose > 0: # prints once per run
                print(f"Best eval: {self.best_eval}")
        return self.best_indiv, np.array(self.all_best_evals)

    # TODO: fix
    def resize_population(self) -> None:
        """ Resize the population to match the maximux budget
        """
        self.offspring_list.pop_size = self.budget - self.curr_budget
        self.offspring_list.individuals = self.offspring_list.individuals[:self.offspring_list.pop_size]

    # TODO: fix
    def update_control_vars(self) -> None:
        """ Updates all control variables
        """
        # Update the best individual
        # best individual is in the first position due to selection
        curr_best_eval, _ = self.parents_list.best_fitness(minimize=self.minimize)
        self.all_best_evals.append(curr_best_eval)

        # increment budget and generation counter
        self.curr_budget += self.offspring_list.pop_size
        self.gen_count += 1

        # reset sigmas if patience has been defined
        if self.patience is not None and self.curr_patience >= self.patience:
            if self.verbose > 1:
                print(f"~~ Reinitializing sigmas for generation {self.gen_count}. ~~")
            self.cont_mutation.set_mut_params(self.parents_list)
            self.curr_patience = 0

        if (self.minimize and curr_best_eval < self.best_eval) \
            or (not self.minimize and curr_best_eval > self.best_eval):  # min or max new best conditions
            self.best_indiv = self.parents_list.individuals[0]
            self.best_eval = curr_best_eval
            # increment number of successful generations
            self.better_generations += 1
            # reset patience since we found a new best
            self.curr_patience = 0
            # debug print
            if self.verbose > 1: # prints every time the algorithm finds a new best
                print(f"Generation {self.gen_count} Best eval: {np.round(self.best_eval, 3)}, budget: {self.curr_budget}/{self.budget}")
        else:  # new best not found, increment current patience counter
            if self.verbose > 1:
                print(f"Generation {self.gen_count}, no new best found. Budget: {self.curr_budget}/{self.budget}")
            self.curr_patience += 1
        