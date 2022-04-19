#!/bin/bash

python main_es.py \
-r "Discrete" \
-m "IndividualSigma" \
-s "CommaSelection" \
-e "Rastrigin" \
-min \
-ps 4 \
-os 24 \
-pd 20 \
-b 1000 \
-rep 200 \
-pat 50 \
-v 1 \