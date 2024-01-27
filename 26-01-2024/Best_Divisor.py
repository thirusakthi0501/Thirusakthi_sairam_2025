'''
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is  better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that 13 is better than 31 and that 12 is better than 11.

Given an integer,n , can you find the divisor of n that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints
  0<=n<=10^5

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of 12 can be expressed as {1,2,3,4,6,12}. The divisor whose digits sum to the largest number is 6 (which, having only one digit, sums to itself). Thus, we print 6 as our answer.

'''
#!/bin/python3

import math
import os
import random
import re
import sys

def d(h):
    return sum(int(dd) for dd in str(h))
def s(n):
    b=1
    l=1
    for t in range(2,n+1):
        if n%t==0:
            f=d(t)
            if f>l or (f==l and t<b):
                l=f
                b=t
    return b
if __name__ == '__main__':
    n = int(input().strip())
    r=s(n)
    print(r)
