#!/bin/bash

python src/main_ea.py \
-r "GlobalDiscrete" \
-m "OneSigma" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 6 \
-os 36 \
-pd 50 \
-pat 3 \
-b 5000 \
-rep 1 \
-v 2
