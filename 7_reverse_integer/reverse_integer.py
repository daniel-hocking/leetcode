'''
Description: Given a 32-bit signed integer, reverse digits of an integer.
eg.
Input: 123
Output: 321
eg.
Input: -123
Output: -321
eg.
Input: 120
Output: 21

Written by: Daniel Hocking
Date created: 21/05/2018
Source: https://leetcode.com/problems/reverse-integer/description/
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: i
        """
        if not x:
            return x
        is_negative = x < 0
        rx = str(x).rstrip('0').lstrip('-')[::-1]
        rx = int(rx)
        if rx > (2**31 - 1) or rx < -2**31:
            return 0
        return -1 * rx if is_negative else rx
        

def test_reverse(x):
    '''
    >>> test_reverse(123)
    321
    >>> test_reverse(-123)
    -321
    >>> test_reverse(120)
    21
    >>> test_reverse(1534236469)
    0
    '''
    s = Solution()
    return s.reverse(x)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
