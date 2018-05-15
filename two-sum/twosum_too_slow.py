#!/usr/bin/env python3
#https://leetcode.com/problems/two-sum/#/description

#Given nums = [2, 7, 11, 15], target = 9,
#return [0, 1].
#twoSum([2, 7, 11, 15], 9)
#twoSum([2, 7, 11, 15], 22)

# too slow as it is O(n^2)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num1 = ind1 = count = 0
    ans = []
    for num in nums:
        num1 = num
        ind1 = count
        count_b = count + 1
        for num_b in nums[ind1+1:]:
            if (num1 + num_b) == target:
                ans = [ind1, count_b]
                break
            count_b += 1
        count += 1
    return ans
        
