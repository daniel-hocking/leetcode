#!/usr/bin/env python3
#https://leetcode.com/problems/implement-strstr/#/description

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1

t = Solution()
print(t.strStr('test', 'e'))
print(t.strStr('test', 'z'))
print(t.strStr('test', ''))
print(t.strStr('testa', 'ta'))
print(t.strStr('testa', 'taa'))
