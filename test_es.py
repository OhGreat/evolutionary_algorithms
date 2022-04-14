from signal import Sigmasks
from classes.Population import *
from classes.Recombination import *
from classes.Mutation import *
from classes.Selection import *
from classes.Evaluation import *
from classes.EA import *

def main():
    np.random.seed(0)

    recomb = IntermediateD()
    mutation = IndividualSigma()
    selection = PlusSelection()
    evaluation = Rastringin()

    repetitions = 1000

    ea = EA(minimize=True,
            budget=10000,
            parents_size=4,
            offspring_size=24,
            individual_size=5,
            recombination=recomb,
            mutation=mutation,
            selection=selection,
            evaluation=evaluation,
            verbose=0)

    best_evals = []
    start_time = time.time()
    for _ in range(repetitions):
        _, best_eval = ea.run()
        best_evals.append(best_eval)

    # end timer
    end_time = time.time()
    # print results
    print(f"Run time: {end_time - start_time}")
    print(f"mean best eval: {np.mean(best_evals)} in {repetitions} repetitions")


if __name__ == "__main__":
    main()