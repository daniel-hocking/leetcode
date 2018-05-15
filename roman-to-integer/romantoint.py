#!/usr/bin/env python3
#https://leetcode.com/problems/roman-to-integer/#/description

# romanToInt('VI')  = 6
# romanToInt('XI')  = 11
# romanToInt('IV')  = 4
# romanToInt('MCM')  = 1900

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for i in range(len(s) - 1, -1, -1):
        val = dict_val[s[i]]
        if prev > val:
            val = val * -1
        else:
            prev = val
        total += val
    return total
        
