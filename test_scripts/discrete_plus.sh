#!/bin/bash
echo "test print"

python main_es.py \
-r "Discrete" \
-m "IndividualSigma" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 4 \
-os 24 \
-pd 5 \
-b 10000 \
-rep 50 \
-v 1 \
-seed 0