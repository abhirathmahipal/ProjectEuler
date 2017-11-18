#!/bin/python

import sys

def cal(n):
    return (n * (n+1))/2

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    # using sum to n formula and multiplying is 
    # faster than for loop iteration and checking
    n = n - 1 # everything less than n so reduce 1
    n3 = n / 3
    n5 = n / 5
    n15 = n / 15
    print 3 * cal(n3) + 5 * cal(n5) - 15 * cal(n15)