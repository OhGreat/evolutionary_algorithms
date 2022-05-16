#!/bin/bash

python src/main_ea.py \
-r "GlobalDiscrete" \
-m "IndividualSigma" \
-s "PlusSelection" \
-e "Ackley" \
-min \
-ps 6 \
-os 36 \
-pd 50 \
-pat 100 \
-b 1000 \
-rep 100 \
-v 1 \
-seed 0