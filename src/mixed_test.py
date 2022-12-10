from multiprocessing import Process, Pool
import random
import numpy as np
import time

from EA_multiproc.EA_mixed import EA_mixed
from EA_multiproc.Pop_multiproc import Population_multiproc, Population_mix, Individual
from EA_multiproc.Rec_multiproc import GlobalDiscrete_multiproc
from EA_multiproc.Mut_multiproc import IndividualSigma_multiproc, BitFlip_multiproc
from EA_multiproc.Sel_multiproc import CommaSelection_multiproc
from EA_multiproc.Eval_multiproc import Ackley_multiproc, test

minimize = True
pop_size = 3
off_size = 3*7
ind_size = 500
budget = 5000
discrete = False
patience = 5
verbose=0

choices = [0,1,2,3,4]
val = [2,1,3,1,4,1,2,4,3]
print(val)
new_vals = []
for curr_val in val:
    choices.remove(curr_val)
    new_vals.append(random.choice(choices))
    choices.insert(curr_val,curr_val)
print(new_vals)
exit()

par_cont = Population_multiproc(
    pop_size=pop_size,
    ind_size=ind_size, 
    discrete=discrete,
)
off_cont = Population_multiproc(
    pop_size=off_size,
    ind_size=ind_size, 
    discrete=discrete,
)
par_disc = Population_multiproc(
    pop_size=pop_size,
    ind_size=ind_size, 
    discrete= not discrete,
)
off_disc = Population_multiproc(
    pop_size=off_size,
    ind_size=ind_size, 
    discrete= not discrete,
)

pop = Population_mix(
    pop_size=pop_size,
    ind_size=[ind_size, ind_size],
    discrete=[discrete, not discrete],
)
print(pop.individuals)
exit()

cont_mut = IndividualSigma_multiproc()
# mutation parameters have to be created before calling EA
cont_mut.set_mut_params(par_cont)
cont_mut.set_mut_params(off_cont)

disc_mut = BitFlip_multiproc(p=0.1)

rec = GlobalDiscrete_multiproc()
sel = CommaSelection_multiproc()
ev = test()

ea_pool = EA_mixed(
    minimize=True,
    budget=budget,
    patience=patience, 
    parents_list=[par_cont, par_disc],
    offspring_list=[off_cont, off_disc],
    recombination=[rec, rec],
    mutation=[cont_mut, disc_mut],
    selection=[sel, sel],
    evaluation=ev,
    pool_size=None,
    verbose=verbose,
)
t_start = time.time()
best_ind, best_eval = ea_pool.run()
t_end = time.time()
print(f"EA parallelization time: {np.round(t_end - t_start,3)}, eval: {min(best_eval)}")
