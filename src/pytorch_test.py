from time import time
from EA_numpy.Population import *
from EA_numpy.Recombination import *
from EA_numpy.Mutation import *
from EA_numpy.Selection import *
from EA_numpy.Evaluation import *
from EA_torch.Population_torch import *
from EA_torch.Recombination_torch import *
from EA_torch.Mutation_torch import *
from EA_torch.Selection_torch import *
from EA_torch.Evaluation_torch import *


def main():
    device = "cuda"


    mut = IndividualSigma()
    mut_torch = IndividualSigma_torch(device)

    pop_size=10
    off_size=60
    ind_size = 5000

    pop = Population(pop_size,ind_size, mut)
    off = Population(off_size,ind_size, mut)
    pop_torch = Population_torch(pop_size,ind_size, mut_torch, device)
    off_torch = Population_torch(off_size,ind_size, mut_torch, device)

    rec = Intermediate()
    rec_torch = Intermediate_torch()
    
    sel_torch = CommaSelection_torch()
    sel = CommaSelection()

    eval_ = Bartels()
    eval_torch = Bartels_torch()


    run_EA(pop_torch, off_torch, rec_torch, mut_torch, sel_torch, eval_torch, 1000, 5, True)

# pop_torch.fitnesses = torch.tensor([random.uniform(0.,1.) for _ in pop_torch.individuals])


# print(pop_torch.individuals)
# st_t = time()
# for i in range(1000):
#     eval_torch(pop_torch)
#     eval_torch(off_torch)
#     sel_torch(pop_torch, off_torch)
# end_t = time()
# print(f"Torch selection time: {end_t - st_t}")
# # print(pop_torch.individuals)

# st_t = time()
# for i in range(1000):
#     eval_(pop)
#     eval_(off)
#     sel(pop, off)
# end_t = time()
# print(f"Numpy recomb time: {end_t - st_t}")

# st_t = time()
# for i in range(1000):
#     rec_torch(pop_torch, off_torch)
# end_t = time()
# print(f"Torch recomb time: {end_t - st_t}")

# st_t = time()
# for i in range(1000):
#     rec(pop,off)
# end_t = time()
# print(f"Numpy recomb time: {end_t - st_t}")


# st_t = time()
# for i in range(1000):
#     mut_torch.mutate(pop_torch)
# end_t = time()
# print(f"Torch mutation time: {end_t - st_t}")

# st_t = time()
# for i in range(10000):
#     mut.mutate(pop)
# end_t = time()
# print(f"Individual sigma time: {end_t - st_t}")



def run_EA( pop: Population_torch, off_pop: Population_torch, 
            rec, mut, sel, eval_, 
            budget, patience, minimize,
            verbose=2):

    curr_budget = 0
    curr_gen = 0
    better_gens = 0
    # initial evaluation
    eval_(pop)
    best_eval, best_idx = pop.best_fitness(minimize)
    best_indiv = pop.individuals[best_idx]
    curr_budget += pop.pop_size
    all_best_evals = []

    # debug print
    if verbose > 1: # prints zeneration 0 best eval
        print(f"Generation {curr_gen} Best eval: {np.round(best_eval, 3)}, budget: {curr_budget}/{budget}")


if __name__ == "__main__":
    main()