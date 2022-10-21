#!/bin/bash

python src/main_ea.py \
-r "GlobalDiscrete" \
-m "IndividualSigma" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 6 \
-os 36 \
-pd 50 \
-pat 3 \
-b 50 \
-rep 1 \
-v 2
