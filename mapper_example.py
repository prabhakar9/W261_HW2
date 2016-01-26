#!/usr/bin/python
import os
import re
WORD_RE = re.compile(r"[\w]+")

files = [f for f in os.listdir("/root/hw2") if "wordcount" in f]

for f in files:
    with open(f, "r") as fp:
        for line in fp.readlines():
            for word in WORD_RE.findall(line):
                print '{0}\t{1}'.format(word.lower(), str(1))