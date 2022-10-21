from EA_numpy.Population import *
from EA_numpy.Recombination import *
from EA_numpy.Mutation import *
from EA_numpy.Selection import *
from EA_numpy.Evaluation import *
from EA_numpy.EA import *
from EA_torch.Mutation_torch import *
import time
from copy import deepcopy
import multiprocessing as mp



def main():
    test_iters = 2000

    parents_size = 30
    offspring_size = 30
    individual_size = 5000

    device = "cuda"

    mutation = IndividualSigma()
    gpu_mut = IndividualSigma_torch(device)
    mut_multiprocess = IndividualSigma_multiprocess()

    offspring = Population(offspring_size, 
                            individual_size, 
                            mutation)
    off_gpu = Population_torch(offspring_size, 
                                individual_size, 
                                gpu_mut, device=device)

    parallel_offs  = [Population(1,individual_size, mutation) 
                        for _ in range(offspring_size)]
    # print()

    # no parallel loop
    t_start = time.time()
    for _ in range(test_iters):
        mutation(offspring)
    t_end = time.time()
    print(f"No parallelization time: {np.round(t_end - t_start,3)}")

    t_start = time.time()
    for _ in range(test_iters):
        gpu_mut.mutate(off_gpu)
    t_end = time.time()
    print(f"Torch gpu time: {np.round(t_end - t_start,3)}")


    # parallel execution
    t_start = time.time()
    pool = mp.Pool(mp.cpu_count())
    for _ in range(test_iters):
        ret = pool.map_async(mut_multiprocess.mutate, parallel_offs)
    
    # print(ret)
    pool.close()
    res = ret.get()
    for off, x in zip(parallel_offs, res):
        off.individuals = x[0]
        off.sigmas = x[1]
    
        # print()
            # off.individuals, off.sigmas = ret[0], ret[1]
            
    pool.close()
    pool.join()
    t_end = time.time()
    print(f"Parallelization time: {np.round(t_end - t_start,3)}")


def get_result(result):
    global results
    results.append(result)

if __name__ == "__main__":
    main()