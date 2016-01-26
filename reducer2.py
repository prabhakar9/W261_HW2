#!/usr/bin/python
## reducer-2.py
## Author: Prabhakar Gundugola
## Description: reducer-2 code for HW2.3

import sys

count = 0
correct = 0
wrong = 0
zero_probs_spam = 0
zero_probs_ham = 0

for line in sys.stdin:
    tokens = line.strip().split('\t')
    spam, predicted = int(tokens[1]), int(tokens[2])
    count += 1
    zero_probs_spam += int(tokens[5])
    zero_probs_ham += int(tokens[6])
    if spam == predicted:
        correct += 1
    else:
        wrong += 1
    
    print line

training_error = 100.0*wrong/count
accuracy = 100.0*correct/count

print 'Training error: {0}%'.format(training_error)
print 'Accuracy: {0}%'.format(accuracy)