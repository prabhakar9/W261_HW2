#!/usr/bin/python
import sys
for line in sys.stdin:
    key, value = line.strip().split(',')
    print '{0},{1}'.format(key, value)