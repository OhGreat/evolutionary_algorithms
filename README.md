# Evolutionary Strategies Framework

This repository contains a framework for applying evolutionary strategies (ES) on arbitrary black box optimization problems.

## Implementation

The following ES steps have been implemented:
 - **Recombination**: *Intermediate*, *GlobalIntermediary*, *Discrete*, *GlobalDiscrete*
 - **Mutation**: *IndividualSigma*, *IndividualOneFifth*, *(CMA to be added)*
 - **Selection**: (μ + λ) - *PlusSelection*, (μ , λ) - *CommaSelection*
<br/><br/>

The following optimization problems have been implemented:
 - **Ackley**
 - **Adjiman**
 - **Rastrigin**
 - **Thevenot**
 - **Bartels**

## How to use

### Prerequisites

A `Python 3` environment is required, with the packages found in the `requirements.txt` file in the main directory. To install them, run from `main directory` the following command:
```
pip install -r requirements.txt
```

### Usage

The main file to run experiments is the `main_es.py` file in the main directory. A detailed description of all the configurable parameters is available below. Example shell scripts have also been created as an example to set arguments, under the *test_scripts* directory.

### Arguments

The following arguments can be set when running `main_es.py`:

- `-r` : defines the recombination type. Available options: *"Intermediate"*, *"GlobalIntermediary"*, *"Discrete"*, *"GlobalDiscrete"*.
- `-m` : defines the mutation type. Available options: *"IndividualSigma"*, *"IndividualOneFifth"*.
- `-s` : defines the selection type. Available options: *"PlusSelection"*, *"CommaSelection"*.
- `-e` : defines the evaluation type. Available options: *"Rastrigin"*, *"Ackley"*, *"Thevenot"*, *"Adjiman"*, *"Bartels"*. If an evaluation function is not defined, all the above functions will be used.
- `-min` : set this flag if the optimization problem is minimization.
- `-ps` : defines the number of parents. Should be an integer value.
- `-os` : defines the number of offsprings. Should be an integer value.
- `-pd` : defines the problem dimension. Will be used to set the individual size.
- `-mul` : defines the multiplier for the IndividualOneFifth mutation. Float value, default is *0.9*.
- `-pat` : defines the number of unsuccesful generations to wait before resetting sigmas.
- `-b` : defines the budget. Should be an integer value.
- `-rep` : defines the number of repetitions to average results. Should be an integer value.
- `-v` : defines the verbose (prints) intensity. Available options are: *0*, *1*, *2* ,with *2* being the most intense. 
- `-seed` : defines the seed to use for reproducibility of results. Set to an integer value.
- `-save_plots` : set the flag in order to save plots of the algorithms performance.

### Creating your own evaluation functions 

To create your own evaluation function you can extend the `Evaluate` class on the `Evaluation.py` file in the `classes` folder. Each evaluation class should have at least the __call__ methods defined to work properly.

## Examples

The following image is the result of the `individual.sh` configuration found in the `test_scripts` directory.

<img src="https://github.com/OhGreat/evolutionary_algorithms/blob/main/readme_aux/example_plots.png" />

## Future Work

- ~~add more optimization problems~~
- ~~implement One Fifth rule~~
- implement CMA-ES mutation strategy
- implement upsampling
- ~~implement more recombination types~~
- add possibility to use IOH experimenter
