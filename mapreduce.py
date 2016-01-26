#!/usr/bin/python
## mapper.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW2.2.1
import sys

#Swap key and value
for line in sys.stdin:
    vals = line.replace('\n', '').split('\t')
    print('{0}\t{1}'.format(vals[1], vals[0]))