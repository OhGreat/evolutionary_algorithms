#!/bin/bash

python main_es.py \
-r "Discrete" \
-m "IndividualSigma" \
-s "CommaSelection" \
-e "Rastrigin" \
-min \
-ps 4 \
-os 24 \
-pd 5 \
-b 10000 \
-rep 10 \
-v 1 \
-seed 0