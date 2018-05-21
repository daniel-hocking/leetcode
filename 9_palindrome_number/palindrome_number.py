'''
Description: Determine whether an integer is a palindrome. An integer is a
palindrome when it reads the same backward as forward.
eg.
Input: 121
Output: true
eg.
Input: -121
Output: false
eg.
Input: 10
Output: false

Written by: Daniel Hocking
Date created: 21/05/2018
https://leetcode.com/problems/palindrome-number/description/
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)
        return str_x == str_x[::-1]

    def isPalindromeNoStr(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x == 0:
            return True
        if x % 10 == 0 or x < 0:
            return False

        x_rev = 0
        x_mod = x
        while x_mod:
            x_rev *= 10
            x_rev += x_mod % 10
            x_mod //= 10
        return x == x_rev
        

def test_is_palindrome(x):
    '''
    >>> test_is_palindrome(121)
    True
    >>> test_is_palindrome(-121)
    False
    >>> test_is_palindrome(10)
    False
    >>> test_is_palindrome(101)
    True
    '''
    s = Solution()
    return s.isPalindrome(x)

def test_is_palindrome_no_str(x):
    '''
    >>> test_is_palindrome_no_str(121)
    True
    >>> test_is_palindrome_no_str(-121)
    False
    >>> test_is_palindrome_no_str(10)
    False
    >>> test_is_palindrome_no_str(101)
    True
    >>> test_is_palindrome_no_str(0)
    True
    '''
    s = Solution()
    return s.isPalindromeNoStr(x)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
