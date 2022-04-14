from classes.Population import *
from classes.Recombination import *
from classes.Mutation import *
from classes.Selection import *
from classes.Evaluation import *
from classes.EA import *
import time


def main():
    random.seed(0)
    np.random.seed(0)

    recombination = Intermediate()
    mutation = IndividualSigma()
    selection = PlusSelection()
    evaluation = Ackley()

    repetitions = 1000

    ea = EA(minimize=True,
            budget=10000,
            parents_size=4,
            offspring_size=24,
            individual_size=5,
            recombination=recombination,
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
    end_time = time.time()

    # print results
    print()
    print(f"Run time: {np.round(end_time - start_time, 3)}")
    print(f"mean best eval: {np.round(np.mean(best_evals),4)}, mean budget: {np.mean(best_budgets)}, in {repetitions} repetitions")


if __name__ == "__main__":
    main()