#!/bin/bash

python main_es.py \
-r "GlobalDiscrete" \
-m "IndividualSigma" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 3 \
-os 20 \
-pd 5 \
-b 10000 \
-rep 500 \
-v 1 \
-seed 11