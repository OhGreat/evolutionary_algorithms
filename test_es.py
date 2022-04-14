from signal import Sigmasks
from classes.Population import *
from classes.Recombination import *
from classes.Mutation import *
from classes.Selection import *
from classes.Evaluation import *
from classes.EA import *

random.seed(0)
np.random.seed(0)

def main():

    recomb = Intermediate()
    mutation = OneFifth()
    selection = PlusSelection()
    evaluation = Rastringin()

    repetitions = 1

    ea = EA(minimize=True,
            budget=10000,
            parents_size=2,
            offspring_size=4,
            individual_size=5,
            recombination=recomb,
            mutation=mutation,
            selection=selection,
            evaluation=evaluation,
            verbose=0)

    best_evals = []
    best_budgets = []
    start_time = time.time()
    for _ in range(repetitions):
        _, best_eval, best_budget = ea.run()
        best_evals.append(best_eval)
        best_budgets.append(best_budget)

    # end timer
    end_time = time.time()
    # print results
    print(f"Run time: {end_time - start_time}")
    print(f"mean best eval: {np.mean(best_evals)}, budget: {np.mean(best_budgets)}, in {repetitions} repetitions")


if __name__ == "__main__":
    main()