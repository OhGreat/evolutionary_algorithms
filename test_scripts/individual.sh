#!/bin/bash

python main_ea.py \
-r "Discrete" \
-m "IndividualSigma" \
-s "CommaSelection" \
-e "Ackley" "Adjiman" "Thevenot" "Rastrigin" "Bartels" \
-min \
-ps 3 \
-os 21 \
-pd 40 \
-b 10000 \
-pat 30 \
-rep 5 \
-save_plots \
-v 0
