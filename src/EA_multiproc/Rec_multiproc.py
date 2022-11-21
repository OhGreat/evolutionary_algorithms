import numpy as np

from EA_multiproc.Pop_multiproc import Population_multiproc
from EA_numpy.Recombination import Recombination

class GlobalDiscrete_multiproc(Recombination):
    """ Creates discrete recombined offsprings.
    """
    def __init__(self):
        self.curr_parents = None

    def __call__(self, offspring: Population_multiproc):
        if self.curr_parents is None:
            exit("Recombination current parents not defined")
        # rng
        parent_choices = np.random.choice(range(self.curr_parents.pop_size), size=offspring.size)

        # create new offspring
        new_vals = np.array([self.curr_parents.individuals[choice].values[i] for i, choice in enumerate(parent_choices)])
        
        # recombine mutation parameters if required
        if self.curr_parents.has_mut_params:
            new_mut_params =np.array([self.curr_parents.individuals[choice].mut_params[i] for i, choice in enumerate(parent_choices)])
        else: new_mut_params = None
        # revert arrays to numpy
        return new_vals, new_mut_params