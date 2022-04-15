from classes.Population import *
from classes.Recombination import *
from classes.Mutation import *
from classes.Selection import *
from classes.Evaluation import *
from classes.EA import *
import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store',
                        dest='recombination', type=str,
                        default=None)
    parser.add_argument('-m', action='store',
                        dest='mutation', type=str,
                        default='IndividualSigma')
    parser.add_argument('-s', action='store',
                        dest='selection', type=str,
                        default='PlusSelection')
    parser.add_argument('-e', action='store',
                        dest='evaluation', type=str,
                        default='Rastrigin')
    parser.add_argument('-min', action='store_true', 
                        dest='minimize',
                        help="Use this flag if the problem is minimization")
    parser.add_argument('-ps', action='store',
                        dest='parent_size', type=int,
                        default=4)
    parser.add_argument('-os', action='store',
                        dest='offspring_size', type=int,
                        default=24)
    parser.add_argument('-pd', action='store',
                        dest='problem_dimension', type=int,
                        default=5,
                        help="Will define the size of each individual")
    parser.add_argument('-b', action='store',
                        dest='budget', type=int,
                        default=10000)
    parser.add_argument('-rep', action='store',
                        dest='repetitions', type=int,
                        default=100)
    parser.add_argument('-v', action='store',
                        dest='verbose', type=int,
                        default=1)
    parser.add_argument('-seed', action='store',
                        dest='seed', type=int,
                        default=None)
    args = parser.parse_args()
    print()
    print("Arguments passed:")
    print(args)

    if args.seed != None:
        random.seed(args.seed)
        np.random.seed(args.seed)

    # define Evolutionary Strategy
    ea = EA(minimize=args.minimize,
            budget=args.budget,
            parents_size=args.parent_size,
            offspring_size=args.offspring_size,
            individual_size=args.problem_dimension,
            recombination=globals()[args.recombination](),
            mutation=globals()[args.mutation](),
            selection=globals()[args.selection](),
            evaluation=globals()[args.evaluation](),
            verbose=args.verbose)

    # Repeat experiment for n = 'repetitions' times
    repetitions = args.repetitions
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