from multiprocessing import Process, Pool
import time
from EA_numpy.Population import *
from EA_numpy.Recombination import *
from EA_numpy.Mutation import *
from EA_numpy.Selection import *
from EA_numpy.Evaluation import *
from EA_numpy.EA_pool import *
from EA_numpy.EA import *



# multi_mut_2 = IndividualSigma_multiprocess_()
# mut = IndividualSigma()

# pop_ind = [Individual(size=ind_size, discrete=False, mutation=multi_mut) for _ in range(pop_size)]
# pop_ind_2 = Individual_population(pop_size=pop_size, ind_size=ind_size, 
#                                 discrete=False, mutation=multi_mut).individuals

minimize = True
pop_size = 4
off_size = 4*7
ind_size = 5000
budget = 5000
discrete = False
patience = 5
verbose=1


pop_ind = Individual_population(
    pop_size=pop_size,
    ind_size=ind_size, 
    discrete=discrete,
)
off_ind = Individual_population(
    pop_size=off_size,
    ind_size=ind_size, 
    discrete=discrete,
)
mut = IndividualSigma_multiprocess()
mut.set_mut_params(pop_ind)
mut.set_mut_params(off_ind)
rec = GlobalDiscrete_ind()
sel = CommaSelection_ind()
ev = Ackley_ind()

m = IndividualSigma()
pop = Population(
    pop_size,
    ind_size,
    False,
    mutation=m
)
off_pop = pop = Population(
    off_size,
    ind_size,
    False,
    mutation=m,
)
rec_ = GlobalDiscrete()
sel_ = CommaSelection()
ev_ = Ackley()
ea = EA(minimize=minimize, budget=budget, patience=patience,
        parents_size=pop_size, offspring_size=off_size, individual_size=ind_size,
        discrete=discrete, recombination=rec_, mutation=m, selection=sel_, evaluation=ev_, verbose=verbose)
t_start = time.time()
best_ind, best_eval = ea.run()
t_end = time.time()
print(f"EA no parallelization time: {np.round(t_end - t_start,3)}, eval: {max(best_eval)}")

# no parallel loop
# t_start = time.time()
# for _ in range(budget):
#     rec_(pop, off_pop)
# t_end = time.time()
# print(f"No parallelization time: {np.round(t_end - t_start,3)}")

# # Parallelization
# t_start = time.time()
# pool = Pool(1000)
# rec.curr_parents = pop_ind
# for _ in range(budget):
#     res = pool.map(func=mut, iterable=off_ind.individuals)
#     for ind, new_vals in zip(off_ind.individuals, res):
#         ind.values = new_vals[0]
#         ind.mut_params = new_vals[1]
# t_end = time.time()
# print(f"Rec parallelization time: {np.round(t_end - t_start,3)}")

ea_pool = EA_pool(minimize=True, budget=budget, patience=patience, 
                parents=pop_ind, offsprings=off_ind,
                recombination=rec, mutation=mut, selection=sel, evaluation=ev,
                pool_size=None, verbose=verbose)


t_start = time.time()
best_ind, best_eval = ea_pool.run()
t_end = time.time()
print(f"EA parallelization time: {np.round(t_end - t_start,3)}, eval: {max(best_eval)}")




# # async
# t_start = time.time()
# procs = []
# p = Pool(pop_size)
# res = p.map_async(func=multi_mut_2.mutate, iterable=pop_ind_2).get()
# for _ in range(trials):
#     for ind, curr_ in zip(pop_ind_2,res):
#         ind.values = curr_[0]
#         ind.mut_params = curr_[1]
# t_end = time.time()
# p.close()
# print(f"Async parallelization time: {np.round(t_end - t_start,3)}")
# # print(pop_ind_2[0].values)


# t_start = time.time()
# for _ in range(budget):
#     rec(pop_ind)
# t_end = time.time()
# print(f"Parallelization time: {np.round(t_end - t_start,3)}")

