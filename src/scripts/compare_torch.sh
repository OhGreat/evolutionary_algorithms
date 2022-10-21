#!/bin/bash

python src/main_ea.py \
-m "IndividualSigma" \
-s "CommaSelection" \
-e "Adjiman" \
-min \
-ps 20 \
-os 140 \
-pd 500 \
-pat 3 \
-b 2000 \
-rep 1 \
-v 2
