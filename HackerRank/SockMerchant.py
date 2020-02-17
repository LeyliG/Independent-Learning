'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks 
with matching colors there are.

For example, there are n=7 socks with colors ar = [1,1,2,1,2,3,1]. 
There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. The number of pairs is 2.

Function Description
It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Input Format

The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

Constraints
n in [1,100]
ar[i] in [1,100], i in [0,n]


Output Format
Return the total number of matching pairs of socks that John can sell.
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
# Complete the sockMerchant function below.

    # check if the constraints for n and lenght(ar) are satisfied
    if n not in range(1, 101) and len(ar) not in range(1, 101):
        return false

# if the constraints are satified
    # initialize count to count number of pairs
    # and i to loop throught ar 
    count = 0
    i = 0

    # Use sort function to sort all elements of the ar list
    ar.sort()
    
    # loop through the sorted ar list
    # if ith and consecutive element are equal, 
    # incrment count by 1 and i by 2
    # else only increment i by 1
    while i < len(ar)-1:
        if ar[i] == ar[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count

# end of code


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
