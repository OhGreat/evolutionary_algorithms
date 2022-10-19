from time import time

from EA_components_OhGreat.Population import Population
from EA_components_OhGreat.Mutation import IndividualSigma, OneSigma
from EA_components_OhGreat.Recombination import GlobalDiscrete

device = "cuda"

# mut_torch = IndividualSigma_torch(device)

# rec_torch = GlobalDiscrete_torch(device=device)

pop = Population(30,500)
# pop_torch = Population_torch(10,5000, mut_torch, device)

off = Population(30,5000)
# off_torch = Population_torch(30,5000, mut_torch, device)
rec = GlobalDiscrete()
mut = IndividualSigma()
mut_one = OneSigma()

pop.sigma_init(mut)

# st_t = time()
# for i in range(100):
#     rec_torch(pop_torch, off_torch)
# end_t = time()
# print(f"Torch recomb time: {end_t - st_t}")

# st_t = time()
# for i in range(100):
#     rec(pop,off)
# end_t = time()
# print(f"Numpy recomb time: {end_t - st_t}")


# st_t = time()
# for i in range(1000):
#     mut_torch.mutate(pop_torch)
# end_t = time()
# print(f"Torch mutation time: {end_t - st_t}")
st_t = time()
for i in range(10000):
    mut_one.mutate(pop)
end_t = time()
print(f"One sigma time: {end_t - st_t}")

st_t = time()
for i in range(10000):
    mut.mutate(pop)
end_t = time()
print(f"Individual sigma time: {end_t - st_t}")




