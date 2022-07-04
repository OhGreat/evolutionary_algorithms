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
-pat 100 \
-b 5000 \
-rep 100 \
-v 0
