#!/usr/bin/env python2
from __future__ import print_function
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split("\t", 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print("{}\t{}".format(current_word, current_count))
        current_word = word
        current_count = count

# Output the last word
if current_word:
    print("{}\t{}".format(current_word, current_count))
