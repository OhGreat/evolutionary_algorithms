#!/bin/bash
echo "one fifth success rule"
python main_es.py \
-r "Discrete" \
-m "OneFifth_" \
-s "PlusSelection" \
-e "Rastrigin" \
-min \
-ps 4 \
-os 24 \
-pd 5 \
-b 10000 \
-rep 20 \
-v 1