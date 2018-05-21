'''
Description: Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
eg.
Input: "()"
Output: true
eg.
Input: "()[]{}"
Output: true
eg.
Input: "(]"
Output: false
eg.
Input: "([)]"
Output: false
eg.
Input: "{[]}"
Output: true

Written by: Daniel Hocking
Date created: 21/05/2018
https://leetcode.com/problems/valid-parentheses/description/
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        str_len = len(s)
        stack = []
        match_paren = {'(': ')', '[': ']', '{': '}'}
        for i in range(str_len):
            if s[i] in match_paren:
                stack.append(s[i])
            elif len(stack) and s[i] == match_paren[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
            

def test_valid_paren(s):
    '''
    >>> test_valid_paren('()')
    True
    >>> test_valid_paren('()[]{}')
    True
    >>> test_valid_paren('(]')
    False
    >>> test_valid_paren('([)]')
    False
    >>> test_valid_paren('{[]}')
    True
    >>> test_valid_paren('')
    True
    '''
    sol = Solution()
    return sol.isValid(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
