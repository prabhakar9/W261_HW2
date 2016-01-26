#!/usr/bin/python
import sys

def wcount(prev_word, count):
    if prev_word is not None:
        print prev_word.ljust(20) + "\t" + str(count)

prev_word = None
count = 0
for line in sys.stdin:
    word, value = line.split('\t', 1)
    if word != prev_word:
        wcount(prev_word, count)
        prev_word = word
        count = 0
    count += eval(value)
wcount(prev_word, count)