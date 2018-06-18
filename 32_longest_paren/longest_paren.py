'''
Description: Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.
eg.
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
eg.
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Written by: Daniel Hocking
Date created: 18/06/2018
https://leetcode.com/problems/longest-valid-parentheses/description/
'''

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        parens = list(s)
        changed = True
        while changed:
            changed = False
            parens_len = len(parens)
            parens_temp = list(parens)
            for i in range(parens_len - 1, 0, -1):
                if parens_temp[i] == ')':
                    if parens_temp[i - 1] == '(':
                        parens.pop(i)
                        parens[i - 1] = 2
                        changed = True
                    elif isinstance(parens_temp[i - 1], int) and (i - 2) >= 0 and \
                         parens_temp[i - 2] == '(':
                        parens.pop(i)
                        parens[i - 1] += 2
                        parens.pop(i - 2)
                        changed = True
                if isinstance(parens_temp[i], int) and isinstance(parens_temp[i - 1], int):
                    parens[i - 1] += parens.pop(i)
                    changed = True

        parens = list(filter(lambda x: isinstance(x, int), parens))
        return max(parens) if parens else 0
            

def test_longest_paren(s):
    '''
    >>> test_longest_paren('')
    0
    >>> test_longest_paren('(')
    0
    >>> test_longest_paren('(()')
    2
    >>> test_longest_paren(')()())')
    4
    >>> test_longest_paren('()()()')
    6
    >>> test_longest_paren('()(()')
    2
    >>> test_longest_paren('(()())')
    6
    >>> test_longest_paren('()(())')
    6
    >>> test_longest_paren(')()())()()(')
    4
    '''
    sol = Solution()
    return sol.longestValidParentheses(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
