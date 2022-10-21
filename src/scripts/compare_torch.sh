#!/bin/bash

python src/main_ea.py \
-r "Intermediate" \
-m "IndividualSigma" \
-s "CommaSelection" \
-e "Adjiman" \
-min \
-ps 20 \
-os 140 \
-pd 50000 \
-pat 3 \
-b 5000 \
-rep 1 \
-v 2
