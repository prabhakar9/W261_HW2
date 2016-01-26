#!/usr/bin/python
## mapper231.py
## Author: Prabhakar Gundugola
## Description: mapper-1 code for HW2.3

import sys
import re
import string

WORD_RE = re.compile(r"[\w']+") # Compile regex to easily parse complete words

spam_email_count = 0
ham_email_count = 0

total_ham_count = 0
total_spam_count = 0

for line in sys.stdin:
    
    # Tokenize each line. Line format - DOC_ID <tab> SPAM <tab> subject <tab> body
    tokens = line.lower().strip().split('\t')
    
    spam = tokens[1]
    if spam == '1':
        spam_email_count += 1
    else:
        ham_email_count += 1
    
    # Concatenate subject and body fields and store it in word_string
    word_string = tokens[2].strip() + ' ' + tokens[3].strip()
    
    # Remove punctuation
    word_string = word_string.translate(string.maketrans("", ""), 
                                       string.punctuation)
    
    word_list = WORD_RE.findall(word_string)
    # Get unique words
    unique_words = set(word_list)
    
    for word in unique_words:
        word_freq = word_list.count(word)
        print('{0}\t{1}\t{2}'.format(word, spam, str(word_freq)))

print('{0}\t{1}\t{2}'.format('0000000DOC_CLASS', 
                                   str(spam_email_count), 
                                   str(ham_email_count)))          