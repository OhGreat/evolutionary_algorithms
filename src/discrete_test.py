from EA_numpy.Population import *
from EA_numpy.Recombination import *
from EA_numpy.Mutation import *
from EA_numpy.Selection import *
from EA_numpy.Evaluation import *
from EA_numpy.EA import *
from EA_numpy.Crossover import *

ea = EA(minimize=False,budget=1000, patience=None,
    parents_size=6, individual_size=50, offspring_size=42, discrete=True, 
    recombination=GlobalDiscrete(), mutation=BitFlip(p=0.05), selection=PlusSelection(), evaluation=OneMax(),
    verbose=2)

ea.run()