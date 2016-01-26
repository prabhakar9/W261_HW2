#!/usr/bin/python
## mapper-2.py
## Author: Prabhakar Gundugola
## Description: mapper-2 code for HW2.3

import sys
from math import log, exp
import re
import string

WORD_RE = re.compile(r"[\w']+")

words = {}
zero_probs_spam = 0
zero_probs_ham = 0

with open('hw23out.txt', 'rb') as fp:
    for line in fp.readlines():
        tokens = line.strip().split('\t')
        if tokens[0] == "0000000PRIORS":
            prior_spam, prior_ham = float(tokens[1]), float(tokens[2])
            continue
        
        words[tokens[0]] = {'p_spam':float(tokens[1]), 'p_ham':float(tokens[2])}

count = 0        
for line in sys.stdin:
    tokens = line.strip().split('\t')
    count += 1
    
    # Concatenate subject and body fields and store it in word_string
    word_string = tokens[2] + ' ' + tokens[3].strip()
    
    # Remove punctuation
    word_string = word_string.translate(string.maketrans("", ""), 
                                       string.punctuation)
    
    word_list = WORD_RE.findall(word_string)
    
    prior_spam_doc, prior_ham_doc = prior_spam, prior_ham
    
    for word in word_list:
        word = word.lower().strip()
        try:
            if words[word]['p_spam'] <> 0:
                prior_spam_doc += words[word]['p_spam']
            else:
                prior_spam_doc += float('-inf')
                zero_probs_spam += 1
        
            if words[word]['p_ham'] <> 0:
                prior_ham_doc += words[word]['p_ham']
            
            else:
                prior_ham_doc += float('-inf')
                zero_probs_ham += 1
        except:
            continue
            
        
    predicted = 0
    if prior_spam_doc == float('-inf'):
        predicted = 0
        prior_spam_doc = 0
    elif prior_ham_doc == float('-inf'):
        predicted = 1
        prior_ham_doc = 0
    elif prior_spam_doc > prior_ham_doc:
        predicted = 1

    values = tokens[1] + '\t' + str(predicted) + '\t' + str(prior_spam_doc) 
    values += '\t' + str(prior_ham_doc) + '\t' + str(zero_probs_spam)
    values += '\t' + str(zero_probs_ham)
    print tokens[0] + '\t' + values
    
        