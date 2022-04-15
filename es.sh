#!/bin/bash

python test_es.py \
-r "Intermediate" \
-m "IndividualSigma" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 4 \
-os 24 \
-pd 5 \
-b 20000 \
-rep 50 \
-v 1 \
-seed 1