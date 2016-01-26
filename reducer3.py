#!/usr/bin/python
## reducer3.py
## Author: Prabhakar Gundugola
## Description: reducer3 code for HW2.4

import sys
import math

spam_email_count = 0
ham_email_count = 0

spam_word_count = 0
ham_word_count = 0

total_spam_count = 0
total_ham_count = 0

total_docs = 0

spam_words_freq = {}
ham_words_freq = {}

priors_calc = 0

for line in sys.stdin:
    tokens = line.strip().split('\t')
    
    if tokens[0] == "0000000DOC_CLASS":
        spam_email_count = int(tokens[1])
        ham_email_count = int(tokens[2])
        continue
    
    try:
        count = int(tokens[2])
        spam = int(tokens[1])
    except ValueError:
        continue
   
    
    word, spam, frequency = tokens[0], spam, count
    if spam == 1:
        total_spam_count += frequency
        if word in spam_words_freq:
            spam_words_freq[word] += frequency
        else:
            spam_words_freq[word] = frequency
        
        if word not in ham_words_freq:
            ham_words_freq[word] = 0
    else:
        total_ham_count += frequency
        if word in ham_words_freq:
            ham_words_freq[word] += frequency
        else:
            ham_words_freq[word] = frequency
        
        if word not in spam_words_freq:
            spam_words_freq[word] = 0
            
prior_spam = math.log(1.0*spam_email_count/(spam_email_count + ham_email_count))
prior_ham = math.log(1.0*ham_email_count/(spam_email_count + ham_email_count))   
print('{0}\t{1}\t{2}'.format("0000000PRIORS", str(prior_spam), str(prior_ham)))


# Calculate conditional probability. 
# Applied Laplace smoothing to math.log function in the numerator
prob_spam_words = {}
prob_ham_words = {}

for word in ham_words_freq:
    if spam_words_freq[word] > 0:
        prob_spam_words[word] = math.log((1.0)*(spam_words_freq[word]+1)/total_spam_count)
    else:
        prob_spam_words[word] = 0
    if ham_words_freq[word] > 0:
        prob_ham_words[word] = math.log((1.0)*(ham_words_freq[word]+1)/total_ham_count)
    else:
        prob_ham_words[word] = 0
    
    print('{0}\t{1}\t{2}'.format(word, str(prob_spam_words[word]), str(prob_ham_words[word])))
    