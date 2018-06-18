'''
Description: You are a professional robber planning to rob houses along a
street. Each house has a certain amount of money stashed, the only
constraint stopping you from robbing each of them is that adjacent houses
have security system connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight
without alerting the police.
eg.
Input: [2,7,9,3,1]
Output: 12
eg.
Input: [1,2,3,1]
Output: 4

Written by: Daniel Hocking
Date created: 18/06/2018
https://leetcode.com/problems/house-robber/description/
'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_len = len(nums)
        if num_len == 1:
            return nums[0]
        check_1 = [[nums[0]], nums[0], True]
        check_2 = [[], 0, False]
        for i in range(1, num_len):
            if check_1[2] and not check_2[2] and \
               check_1[1] <= check_2[1]:
                check_1[0] = list(check_2[0])
                check_1[1] = check_2[1]
                check_1[2] = False
            if not check_1[2] and check_2[2] and \
               check_2[1] <= check_1[1]:
                check_2[0] = list(check_1[0])
                check_2[1] = check_1[1]
                check_2[2] = False
                
            if not check_1[2]:
                check_1[0].append(nums[i])
                check_1[1] += nums[i]
                check_1[2] = True
                check_2[2] = False
            else:
                check_2[0].append(nums[i])
                check_2[1] += nums[i]
                check_2[2] = True
                check_1[2] = False

        
        return max((check_1[1], check_2[1]))
            

def test_rob(nums):
    '''
    >>> test_rob([])
    0
    >>> test_rob([2])
    2
    >>> test_rob([1, 3])
    3
    >>> test_rob([2,7,9,3,1])
    12
    >>> test_rob([1,2,3,1])
    4
    >>> test_rob([9,1,2,1,2,7])
    18
    '''
    s = Solution()
    return s.rob(nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
