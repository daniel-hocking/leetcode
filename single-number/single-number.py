#!/usr/bin/env python3
#https://leetcode.com/problems/valid-palindrome/#/description

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cache_dict = {}
    for i in range(len(nums)):
        #print(nums)
        #print(i)
        #print(cache_dict)
        cur_num = nums[i]
        if cur_num in cache_dict:
            cache_dict.pop(cur_num)
        else:
            cache_dict[cur_num] = i
    return cache_dict.keys()[0]

print('Test: [1, 1, 2, 2, 3]')
print('Expected: 3')
print('Result: '+str(singleNumber([1, 1, 2, 2, 3])))
print('')
    
print('Test: [1, 3, 2, 1, 2]')
print('Expected: 3')
print('Result: '+str(singleNumber([1, 3, 2, 1, 2])))
print('')
