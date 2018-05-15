#!/usr/bin/env python3
#https://leetcode.com/problems/count-and-say/#/description

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num_str = '1'
        if n == 1:
            return num_str
        for i in range(1, n):
            new_num_str = ''
            cur = None
            prev = None
            count = 0
            for l in range(len(num_str)):
                prev = cur
                cur = num_str[l]
                if prev == cur or prev == None:
                    count += 1
                else:
                    new_num_str += str(count) + prev
                    count = 1
            new_num_str += str(count) + cur
            num_str = new_num_str
        return num_str
            

t = Solution()
print('n = 1: '+t.countAndSay(1))
print('n = 2: '+t.countAndSay(2))
print('n = 3: '+t.countAndSay(3))
print('n = 4: '+t.countAndSay(4))
print('n = 5: '+t.countAndSay(5))
print('n = 6: '+t.countAndSay(6))
