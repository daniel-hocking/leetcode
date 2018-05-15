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
    if x < 2:
        return x
    i = round(x / 2)
    prev = x
    keep_looping = True
    while keep_looping:
        test = i * i
        if test == x:
            break
        if (prev * prev) < x and test > x:
            i = prev
            break
        if test > x:
            prev = i
            if abs(prev - i) < 5:
                i -= 1
            else:
                i = round(i / 2)
        else:
            prev = i
            if abs(prev - i) < 5:
                i += 1
            else:
                i += round(i / 2)
    return int(round(i))
