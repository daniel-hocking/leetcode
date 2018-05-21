'''
Description: Given an array of integers, return indices of the two 
numbers such that they add up to a specific target. You may assume
that each input would have exactly one solution, and you may not use
the same element twice.
eg.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Written by: Daniel Hocking
Date created: 21/05/2018
Source: https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_elements = len(nums)
        # Less than two elements then just return empty list
        if num_elements < 2:
            return []

        # Setup a dictionary that will have key: remainder of target - num
        # value: the index of said num
        remainders = {}
        # Iterate over input nums
        for i in range(num_elements):
            if nums[i] in remainders:
                return [remainders[nums[i]], i]
            remainders[target - nums[i]] = i
        # No answer found
        return []

def test_two_sum(nums, target):
    '''
    >>> test_two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> test_two_sum([2, 7, 11, 15], 13)
    [0, 2]
    >>> test_two_sum([2, 7, 11, 15], 22)
    [1, 3]
    >>> test_two_sum([3, 3], 6)
    [0, 1]
    '''
    s = Solution()
    return s.twoSum(nums, target)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
