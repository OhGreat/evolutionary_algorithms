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
                        default=None,
                        help="Defines the recombination strategy.")
    parser.add_argument('-m', action='store',
                        dest='mutation', type=str,
                        default='IndividualSigma',
                        help="Defines the mutation strategy.")
    parser.add_argument('-s', action='store',
                        dest='selection', type=str,
                        default='PlusSelection',
                        help="Defines the selection strategy.")
    parser.add_argument('-e', action='store',
                        dest='evaluation', type=str,
                        default=None,
                        help="Defines the evaluation function.")
    parser.add_argument('-min', action='store_true', 
                        dest='minimize',
                        help="Use this flag if the problem is minimization.")
    parser.add_argument('-ps', action='store',
                        dest='parents_size', type=int,
                        default=4,
                        help="Defines the number of parents per generation.")
    parser.add_argument('-os', action='store',
                        dest='offspring_size', type=int,
                        default=24,
                        help="Defines the number of offspring per generation.")
    parser.add_argument('-pd', action='store',
                        dest='problem_dimension', type=int,
                        default=5,
                        help="Defines the problem dimension which is also the size of each individual.")
    parser.add_argument('-mul', action='store',
                        dest='one_fifth_mul', type=float,
                        default=0.9,
                        help="Defines the multiplier for the one fifth success rule.")
    parser.add_argument('-pat', action='store',
                        dest='patience', type=int,
                        default=None,
                        help="Defines the wait time before resetting sigmas.")          
    parser.add_argument('-b', action='store',
                        dest='budget', type=int,
                        default=10000,
                        help="Defines the total amount of evaluations.")
    parser.add_argument('-rep', action='store',
                        dest='repetitions', type=int,
                        default=100,
                        help="Defines the number of repetitions to average results.")
    parser.add_argument('-v', action='store',
                        dest='verbose', type=int,
                        default=1,
                        help="Defines the intensity of debug prints.")
    parser.add_argument('-seed', action='store',
                        dest='seed', type=int,
                        default=None,
                        help="Defines the seed for result reproducibility.")
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

    # recombination specific control
    if args.recombination != None:
        recombination = globals()[args.recombination]()
    # GlobalIntermediary recombination check
    elif args.recombination == "GlobalIntermediary" and args.offspring_size > 1:
        print("GlobalIntermediary recombination cannot be used with more than one offspring.")
        print("Please use a valid configuration")
        exit()
    else: recombination = None

    # mutation specific controls
    if args.mutation == "IndividualOneFifth":
        mutation = globals()[args.mutation](args.one_fifth_mul)
    else:
        mutation = globals()[args.mutation]()

    selection=globals()[args.selection]()

    # in case we want to evaluate on multiple problems
    if args.evaluation == None:
        print('Evaluation not selected, using all available evaluation functions.')
        evaluation = [Ackley(), Rastrigin(), Thevenot(), Adjiman(), Bartels()]
    else:
        evaluation=[globals()[args.evaluation]()]
    verbose=args.verbose

    if args.seed != None:
        random.seed(args.seed)
        np.random.seed(args.seed)

    # iterate over chosen evaluation functions
    for eval_fun in evaluation:

        # Repeat experiment for n = 'repetitions' times
        repetitions = args.repetitions
        best_evals = []
        start_time = time.time()
        for _ in range(repetitions):
            # define Evolutionary Algorithm
            ea = EA(minimize=minimize,
                    budget=budget,
                    patience=patience,
                    parents_size=parents_size,
                    offspring_size=offspring_size,
                    individual_size=individual_size,
                    recombination=recombination,
                    mutation=mutation,
                    selection=selection,
                    evaluation=eval_fun,
                    verbose=verbose)

            _, best_eval = ea.run()
            best_evals.append(best_eval)
        end_time = time.time()

        # print results
        best = np.min(best_evals) if minimize else np.max(best_evals)
        print(f"{eval_fun.__class__.__name__} - run time: {np.round(end_time - start_time, 2)}")
        print(f"best_eval: {best}, mean eval: {np.round(np.mean(best_evals),4)} in {repetitions} repetitions")
        print()

if __name__ == "__main__":
    main()