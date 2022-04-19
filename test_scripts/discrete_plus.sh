#!/bin/bash

python main_es.py \
-r "Discrete" \
-m "IndividualSigma" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 4 \
-os 24 \
-pd 20 \
-b 1000 \
-pat 100 \
-rep 200 \
-v 1