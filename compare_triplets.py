#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a1,a2, a3, b1, b2, b3):
    score = [0, 0]
    alice = (a1,a2,a3)
    bob = (b1, b2, b3)
    for a, b in zip(alice, bob):
        if a > b:
            score[0] += 1
        elif b > a:
            score[1] += 1
    return score
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a1, a2, a3 = list(map(int, input().rstrip().split()))

    b1, b2, b3 = list(map(int, input().rstrip().split()))

    result = compareTriplets(a1, a2, a3, b1, b2, b3)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
