#!/usr/bin/env python2
from __future__ import print_function
import sys

# Read each line from stdin
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print("{}\t1".format(word))
