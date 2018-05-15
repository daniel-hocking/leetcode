#!/usr/bin/env python3
#https://leetcode.com/problems/two-sum/#/description

#Given nums = [2, 7, 11, 15], target = 9,
#return [0, 1].
#twoSum([2, 7, 11, 15], 9)
#twoSum([2, 7, 11, 15], 22)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    cache = {}
    if len(nums) <= 1:
        return []
    
    for ind in range(len(nums)):
        if (target - nums[ind]) in cache:
            return [cache[target - nums[ind]], ind]
        cache[nums[ind]] = ind
        
