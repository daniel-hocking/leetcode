#!/usr/bin/env python3
#https://leetcode.com/problems/sqrtx/#/description

# mySqrt(9)  = 3
# mySqrt(36)  = 6
# mySqrt(144)  = 12
# mySqrt(900)  = 30

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    i = 0
    for i in range(1, x):
        if (i * i) == x:
            break
    return i
