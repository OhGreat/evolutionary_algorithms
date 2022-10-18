from time import time
import torch
import numpy as np

from src.EA_components_OhGreat.Population import Population
from src.EA_components_OhGreat.Mutation import IndividualSigma
from src.EA_components_OhGreat.Population_torch import Population_torch
from src.EA_components_OhGreat.IndividualSigma_torch import IndividualSigma_torch


device = "cuda"

mut = IndividualSigma()
mut_torch = IndividualSigma_torch(device)

x = Population(30,2000, mut)
y = Population_torch(30,2000, mut_torch, device)



st_t = time()
for i in range(10000):
    mut_torch.mutate(y)
end_t = time()
print(f"New mutation time: {end_t - st_t}")

st_t = time()
for i in range(10000):
    mut.mutate(x)
end_t = time()
print(f"Old mutation time: {end_t - st_t}")

