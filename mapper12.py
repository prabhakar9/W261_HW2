#!/usr/bin/python
## mapper.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW2.2

import sys
import re
import string

# Get user specified words from first argument
word_list = sys.argv[1].split()

## collect user input
for line in sys.stdin:
    tokens = line.lower().split('\t')

    # Concatenate subject and body fields and store it in word_string
    word_string = tokens[2] + ' ' + tokens[3].strip()

    # Remove punctuation
    word_string = word_string.translate(string.maketrans("",""), 
                                        string.punctuation)

    for word in word_string.split():
        if word.lower() in word_list:
            print '{0}\t{1}'.format(word.lower(), 1)