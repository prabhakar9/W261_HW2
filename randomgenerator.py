#!/usr/bin/python
import sys
import random

for i in range(10000):
    sys.stdout.write("{0},{1}\n".format(random.randint(1, 10000), "NA"))