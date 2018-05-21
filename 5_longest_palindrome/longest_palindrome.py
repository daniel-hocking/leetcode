'''
Description: Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
eg.
Input: "babad"
Output: "bab"
eg.
Input: "cbbd"
Output: "bb"

Written by: Daniel Hocking
Date created: 21/05/2018
https://leetcode.com/problems/longest-palindromic-substring/description/
'''

class Solution:
    def _longestPalindrome(self, s):
        if len(s) < 2:
            return s
        if s == s[::-1]:
            return s
        remove_left = self._longestPalindrome(s[1::])
        remove_right = self._longestPalindrome(s[:-1:])
        return max((remove_left, remove_right), key = lambda x: len(x))
        
    def longestPalindromeV2(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2:
            return s
        len_s = len(s)
        rev_s = s[::-1]
        match_list = []
        match_len = longest_match = 0
        match_str = ''
        for i in range(len_s):
            print(s[i])
            if s[i] == rev_s[i]:
                match_list.append(s[i])
                match_len += 1
            elif match_len > 0:
                if match_len > longest_match:
                    longest_match = match_len
                    match_str = ''.join(match_list)
                match_len = 0
                match_list.clear()
        if match_len > longest_match:
            match_str = ''.join(match_list)
        return match_str

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        len_s = len(s)
        if len_s < 2:
            return s
        longest_match = 0
        match_str = ''
        for i in range(len_s):
            if (len_s - i) < longest_match:
                break
            for j in range(len_s, i + longest_match, -1):
                test_str = s[i:j:]
                rev_s = test_str[::-1]
                if test_str == rev_s:
                    match_len = len(test_str)
                    if match_len > longest_match:
                        longest_match = match_len
                        match_str = test_str
                    break
        return match_str
        

def test_longest_palindrome(s):
    '''
    >>> test_longest_palindrome('babad')
    'bab'
    >>> test_longest_palindrome('cbbd')
    'bb'
    >>> test_longest_palindrome('')
    ''
    >>> test_longest_palindrome('c')
    'c'
    >>> test_longest_palindrome('zzzzz')
    'zzzzz'
    >>> test_longest_palindrome('bbbbbbbbaaaaaaaabbbbbbbb')
    'bbbbbbbbaaaaaaaabbbbbbbb'
    >>> test_longest_palindrome('babaddtattarrattatddetartrateedredividerb')
    'ddtattarrattatdd'
    '''
    sol = Solution()
    return sol.longestPalindrome(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
