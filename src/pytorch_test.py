from time import time

from EA_components_OhGreat.Population import Population
from EA_components_OhGreat.Mutation import IndividualSigma, OneSigma
from EA_components_OhGreat.Recombination import *
from EA_torch.Mutation_torch import *
from EA_torch.Population_torch import *
from EA_torch.Recombination_torch import *

device = "cuda"


mut = IndividualSigma()
mut_torch = IndividualSigma_torch(device)

pop = Population(10,50000, mut)
off = Population(50,50000, mut)
pop_torch = Population_torch(10,50000, mut_torch, device)
off_torch = Population_torch(50,50000, mut_torch, device)

rec = Intermediate()
rec_torch = Intermediate_torch()



st_t = time()
for i in range(1000):
    rec_torch(pop_torch, off_torch)
end_t = time()
print(f"Torch recomb time: {end_t - st_t}")

st_t = time()
for i in range(1000):
    rec(pop,off)
end_t = time()
print(f"Numpy recomb time: {end_t - st_t}")


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




