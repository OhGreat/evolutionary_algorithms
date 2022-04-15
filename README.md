# Evolutionary Strategies Framework

This repository contains a framework for applying evolutionary strategies (ES) on arbitrary optimization problems.

## How to use

### Prerequisites

An environment with `Python 3` with the `numpy` package is required. 

### Usage

The main file to run experiments is the `test_es.py` file in the main directory. A detailed description of all the configurable parameters is available below. An example shell script `es.sh` has also been created as an example to set arguments.

### Arguments
The following arguments can be set when running `test_es.py`:

- `-r` : defines the recombination type. Available options: *"Intermediate"*, (more to follow)
- `-m` : defines the mutation type. Available options: *"IndividualSigma"*, (more to follow)
- `-s` : defines the selection type. Available options: *"PlusSelection"*, *"CommaSelection"* (more to follow)
- `-e` : defines the evaluation type. Available options: *"Rastrigin"*, *"Ackley"*, (more to follow)
- `-min` : set this flag if the optimization problem is minimization.
- `-ps` : defines the number of parents. Should be an integer value.
- `-os` : defines the number of offsprings. Should be an integer value.
- `-pd` : defines the problem dimension. Will be used to set the individual size.
- `-b` : defines the budget. Should be an integer value.
- `-rep` : defines the number of repetitions to average results. Should be an integer value.
- `-v` : defines the *verbose* intensity. Available options are: *0*, *1*, *2* ,with *2* being the most intense. 
- `-seed` : defines the seed to use for reproducibility of results. Set to an integer value.


### Creating your own evaluation functions 
To create your own evaluation function you can expand the `Evaluate` class on the `Evaluation.py` file in the `classes` folder.

## Future Work

- implement CMA-ES mutation strategy
- implement One Fifth rule
- implement the upsampling strategy
- impolement more recombination types
