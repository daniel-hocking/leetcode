'''
Description: Given an integer array nums, find the sum of the elements
between indices i and j (i ≤ j), inclusive.
eg.
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Written by: Daniel Hocking
Date created: 18/06/2018
https://leetcode.com/problems/range-sum-query-immutable/description/
'''

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        num_len = len(nums)
        for i in range(num_len):
            self.sums.append(nums[i])
            if i:
                self.sums[i] += self.sums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - (self.sums[i - 1] if i else 0)
            

def test_sum_range(nums, i, j):
    '''
    >>> test_sum_range([-2, 0, 3, -5, 2, -1], 0, 2)
    1
    >>> test_sum_range([-2, 0, 3, -5, 2, -1], 2, 5)
    -1
    >>> test_sum_range([-2, 0, 3, -5, 2, -1], 0, 5)
    -3
    '''
    s = NumArray(nums)
    return s.sumRange(i, j)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
