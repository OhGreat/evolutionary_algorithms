import numpy as np
from typing import List, Tuple


class Individual:
    def __init__(self, size: int, discrete: int = False) -> None:
        """ Initialize individual 
        Args:
        - size: definese the size of the individual
        - discrete: defines the range of integers to sample from
        """
        self.size = size
        self.discrete = discrete
        # initialize individual values
        if discrete:
            self.values = np.random.randint(discrete, size=self.size)
        else:
            self.values = np.random.uniform(0, 1, size=self.size)
        self.mut_params = None # mutation relevant parameters

    def to_str(self):
        return f"Individual: {self.values}"


class Population_multiproc:
    def __init__(
        self,
        pop_size: int,
        ind_size: int,
        discrete: bool = False,
    ) -> None:
        self.pop_size = pop_size
        self.ind_size = ind_size
        self.individuals = [Individual(ind_size, discrete=discrete,) 
                            for _ in range(pop_size)]
        self.has_mut_params = False
        self.fitnesses = np.array([])

    def max_fitness(self) -> Tuple[float, int]:
        """ Return the maximum fitness and its index.
        """
        arg_max = np.argmax(self.fitnesses)
        return self.fitnesses[arg_max], arg_max 

    def min_fitness(self) -> Tuple[float, int]:
        """ Return the minimum fitness and its index.
        """
        arg_min = np.argmin(self.fitnesses)
        return self.fitnesses[arg_min], arg_min

    def best_fitness(self, minimize=True) -> Tuple[float, int]:
        """ Returns the best fitness and index of fittest individual.
            
            Params:
                - minimize: set to True for minimization optimization
        """
        best_arg = np.argmin(self.fitnesses) if minimize else np.argmax(self.fitnesses)
        return self.fitnesses[best_arg], best_arg


class Population_mix:
    def __init__(
        self,
        pop_size: int,
        ind_size: List[int],
        discrete: List[bool], # one for each individual
    ) -> None:
        self.pop_size = pop_size
        self.ind_size = ind_size
        self.discrete = discrete
        # create population
        # each individual is a combination of discrete and continuous parts.
        self.individuals = [[Individual(curr_size, curr_discrete)
                        for curr_size, curr_discrete in zip(ind_size, discrete)]
                        for i in range(pop_size)]

        self.has_mut_params = False
        self.fitnesses = np.array([])

    def max_fitness(self) -> Tuple[float, int]:
        """ Return the maximum fitness and its index.
        """
        arg_max = np.argmax(self.fitnesses)
        return self.fitnesses[arg_max], arg_max 

    def min_fitness(self) -> Tuple[float, int]:
        """ Return the minimum fitness and its index.
        """
        arg_min = np.argmin(self.fitnesses)
        return self.fitnesses[arg_min], arg_min

    def best_fitness(self, minimize=True) -> Tuple[float, int]:
        """ Returns the best fitness and index of fittest individual.
            
            Params:
                - minimize: set to True for minimization optimization
        """
        best_arg = np.argmin(self.fitnesses) if minimize else np.argmax(self.fitnesses)
        return self.fitnesses[best_arg], best_arg