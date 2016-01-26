#!/usr/bin/python
## mapper.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW2.2.1
import sys

#Swap key and value
for line in sys.stdin:
    vals = line.strip().split('\t')
    print('{0}\t{1}'.format(vals[1], vals[0]))