'''
Description: Write a function to find the longest common prefix string
amongst an array of strings. If there is no common prefix, return an
empty string "".
eg.
Input: ["flower","flow","flight"]
Output: "fl"
eg.
Input: ["dog","racecar","car"]
Output: ""

Written by: Daniel Hocking
Date created: 21/05/2018
https://leetcode.com/problems/longest-common-prefix/description/
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        num_strs = len(strs)
        if not num_strs:
            return ''
        
        common_pre = strs[0]
        for i in range(1, num_strs):
            len_pre = len(common_pre)
            for j in range(len_pre, -1, -1):
                if common_pre[:j:] == strs[i][:j:]:
                    common_pre = common_pre[:j:]
                    break
            if not common_pre:
                break
        return common_pre
            

def test_common_prefix(strs):
    '''
    >>> test_common_prefix(["flower","flow","flight"])
    'fl'
    >>> test_common_prefix(["dog","racecar","car"])
    ''
    >>> test_common_prefix(["abc","ab","a"])
    'a'
    '''
    s = Solution()
    return s.longestCommonPrefix(strs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
