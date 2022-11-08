from multiprocessing import Process, Pool
import time
from EA_numpy.Population import *
from EA_numpy.Mutation import *

def copy_res(x):
    print(x)

pop_size = 10
ind_size = 10
trials = 10000

multi_mut = IndividualSigma_multiprocess()
mut = IndividualSigma()

pop_ind = [Individual(ind_size, mutation=multi_mut) 
            for i in range(pop_size)]
print(pop_ind[0].values)

pop = Population(pop_size, ind_size, False, mutation=mut)

# no parallel loop
t_start = time.time()
for _ in range(trials):
    mut(pop)
t_end = time.time()
print(f"No parallelization time: {np.round(t_end - t_start,3)}")

# async
t_start = time.time()
procs = []
p = Pool(pop_size)
res = p.map_async(func=multi_mut.mutate, iterable=pop_ind).get()
for ind, curr_ in zip(pop_ind,res):
    ind.values = curr_[0]
    ind.mut_params = curr_[1]
t_end = time.time()
print(f"Async parallelization time: {np.round(t_end - t_start,3)}")


t_start = time.time()
procs = []
p = Pool(pop_size)
res = p.map(multi_mut.mutate, pop_ind)
for ind, curr_ in zip(pop_ind,res):
    ind.values = curr_[0]
    ind.mut_params = curr_[1]
t_end = time.time()
print(f"Parallelization time: {np.round(t_end - t_start,3)}")
