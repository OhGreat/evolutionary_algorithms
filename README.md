# Evolutionary Algorithms Framework
This repository contains a framework for applying evolutionary strategies (ES) on arbitrary black box optimization problems. The purpose of this package is to facilitate the experimentation of EA in various settings. The original github repository can be found <a href="https://github.com/OhGreat/evolutionary_algorithms">here</a>.

## EA Sequential Usage
The following EA components are executed sequentially and can be used independently from other parts of the package as described below.

### Population class
The population class contains the individuals that are optimized with the EA.
To initialize a population you can use the following commands:
```python
# mutation is also explained below
from EA_sequential.Mutation import IndividualSigma
mut = IndividualSigma()
from EA_sequential.Population import Population
population = Population(pop_size=10, ind_size=8, mutation=mut)
```
where:
- `pop_size` : is an integer value representing the size of the population
- `ind_size` : integer value representing the size of an individual. Can be seen as the problem dimension.
- `mutation` : Mutation type. It is used to initialize sigmas and alphas. Please consult the mutation section to learn more about how to initialize a mutation.

Attributes of the class:
- *all the parameters specified above*
- `individuals`: numpy array of shape (pop_size, ind_size), represents the population's values/solutions.
- `sigmas`: sigma values used in mutation for the *IndividualSigma* mutation.
- `fitnesses`: fitnesses representing how good each solution of the population is.

Methods available:
- `sigma_init`: initializes or resets sigmas, with respect to the mutation defined.
- `max_fitness`: returns the maximum fitness and the index i nthe population.
- `min_fitness`: returns the minimum fitness and the index in the population.
- `best_fitness`: takes as argument a boolean value *minimize*, which is True by default and defines if the problem is minimization.

example usage of methods:
```python
# sigma_init happens inplace, no return value
population.sigma_init()  
# max_fitness returns max value and index
max_fit, max_fit_idx = population.max_fitness()
# min_fitness returns min value and index
min_fit, min_fit_idx = population.min_fitness()
# best_fitness uses the above functions depending on minimize parameter
best_fit, best_fit_idx = population.best_fitness(minimize=True)
```

### Recombination
All the recombinations created are applied *inplace* on the offspring populations (defined similarly to the above example) and there is no return value. The following Recombination classes have been implemented: ***Intermediate***, ***GlobalIntermediary***, ***Discrete***, ***GlobalDiscrete***. All the recombinations take as input the parent and offspring population. The offspring population is used to save the new individuals created and specifies the size of the offspring population. Using the recombinations can be done as in the example below:
```python
from EA_sequential.Recombination import Intermediate
recomb = Intermediate()
recomb(parents, offsprings)
```

### Mutation
The mutations are applied inplace to the population passed and there is no return value. The following mutations have been implemented: **OneSigma**, **IndividualSigma**. You can use it in the following way:
```python
from EA_sequential.Mutation import IndividualSigma
mutation = IndividualSigma()
mutation(offsprings)
```

### Evaluation
Evaluation takes as input a population and assigns to each individual the proper fitness. The fitnesses are applied inlace to the population and there is no return value. The following evaluation functions have been implemented: **Ackley**, **Rastrigin**, **Thevenot**, **Adjiman**, **Bartels**. They can be called as below:
```python
from EA_sequential.Evaluation import Ackley
eval_fun = Ackley()
eval_fun(population)
```
To create your own evaluation function, implement a class with a call method that evaluates the solutions of the `individuals` attribute of the population object and updates its `fitnesses` attribute with a numpy array of *pop_size* length containing the fitnesses of the individuals.

### Selection
The folowing selection mechanisms have been implemented: **PlusSelection**, **CommaSelection**. *PlusSelection* selects the best individuals from both the parent and offspring populations while, *CommaSelection* only selects the parents of the next generation from the offsprings of the current population. Both the selections take as input both the parent and offspring populations. There is no return value and the selected population is saved in the parents' population.

Example:
```python
from EA_sequential.Selection import CommaSelection
selection = ComamSelection()
selection(parents,offsprings)
```

### EA
The EA class incorporates all the above mentioned steps to create an algorithm. It returns the best found offspring and a numpy array of the best evaluation at each generation. It can be used in the following way:
```python
from EA_sequential.EA import EA
ea_alg = EA(minimize=True, budget=2000,
            parents_size=5, offspring_size=30,
            individual_size=12, recombination="Discrete",
            mutation="IndividualSigma", patience=10,
            selection="PlusSelection", evaluation="Ackley",
            verbose=2)
best_solution, evaluations = ea_alg.run() 
```
where:
- `minimize`: (boolean) True if the proble is minimization, False if maximization.
- `budget`: (int) defines the maximum number of evaluations to perform before stopping the algorithm.
- `parents_size`:
- `offspring_size`:
- `individual_size`:
- `recombination`: (string) defines the recombination to use (name should be the same as one of the classes implemented)
- `mutation`: (string) defines the mutation to use (name should be the same as one of the classes implemented)
- `patience`: (int) defines the number of generations to wait before resetting the `sigmas` attribute (tied to the mutation) of the parent population.
- `selection`: (string) defines the selection to use (name should be the same as one of the classes implemented)
- `evaluation`: (string) defines the evaluation function to use (name should be the same as one of the classes implemented)
- `verbose`: (int) defines the density of debug prints while the algorithm runs.

## EA Multiprocess Usage
*Under construction.*
The latest implementation is available in the original github repository in `sec/EA_multiproc`.

An example is available in the file `src/multiprocess_comparison.py`.

## EA on GPU with Pytorch
*Under construction.*

Currently available code for experimentation can be found in the original repository under `src/EA_torch`.

## Examples 
The following image is the result of the `individual.sh` configuration found in the `src/scripts` directory.

<img src="https://github.com/OhGreat/evolutionary_algorithms/blob/main/readme_aux/example_plots.png" />