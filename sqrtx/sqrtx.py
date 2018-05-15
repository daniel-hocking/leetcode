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
    sqrt= x**(.5)
    return int(sqrt)
