from numpy import dtype
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
                        dest='parents_size', type=int,
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
    parser.add_argument('-pat', action='store',
                        dest='patience', type=int,
                        default=40)
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
    print("Arguments passed:")
    print(args)

    # define arguments here to be able to make checks later
    minimize = args.minimize
    budget = args.budget
    patience = args.patience
    parents_size = args.parents_size
    offspring_size = args.offspring_size
    individual_size = args.problem_dimension
    if args.recombination != None:
        recombination = globals()[args.recombination]()
    else: recombination = None
    mutation = globals()[args.mutation]()
    selection=globals()[args.selection]()
    evaluation=globals()[args.evaluation]()
    verbose=args.verbose

    if args.seed != None:
        random.seed(args.seed)
        np.random.seed(args.seed)

    # GlobalIntermediary recombination check
    if args.recombination == "GlobalIntermediary" and args.offspring_size > 1:
        print("GlobalIntermediary recombination cannot be used with more than one offspring.")
        print("Please use a valid configuration")
        exit()

    # make sure the problem is setup properly
    if args.mutation == "OnePlusOneOneFifth":
        if parents_size > 1:
            parents_size = 1
            if verbose > 0:
                print("Using one fifth rule. Parent size changed to 1.")
        if offspring_size > 1:
            offspring_size = 1
            if verbose > 0:
                print("Using one fifth rule. Offspring size changed to 1.") 
        if recombination != None:
            recombination = None
            if verbose > 0:
                print("Using one fifth rule. Recombination disabled.")


    # define Evolutionary Strategy
    ea = EA(minimize=minimize,
            budget=budget,
            patience=patience,
            parents_size=parents_size,
            offspring_size=offspring_size,
            individual_size=individual_size,
            recombination=recombination,
            mutation=mutation,
            selection=selection,
            evaluation=evaluation,
            verbose=verbose)

    # Repeat experiment for n = 'repetitions' times
    repetitions = args.repetitions
    best_evals = []
    start_time = time.time()
    for _ in range(repetitions):
        _, best_eval = ea.run()
        best_evals.append(best_eval)
    end_time = time.time()

    # print results
    print()
    print(f"Run time: {np.round(end_time - start_time, 3)}")
    print(f"mean best eval: {np.round(np.mean(best_evals),6)} in {repetitions} repetitions")


if __name__ == "__main__":
    main()