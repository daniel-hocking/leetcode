#!/usr/bin/env python3
#https://leetcode.com/problems/majority-element/#/description

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache_dict = {}
        for i in range(len(nums)):
            if nums[i] in cache_dict:
                cache_dict[nums[i]] += 1
            else:
                cache_dict[nums[i]] = 1
        import operator
        return max(cache_dict.iteritems(), key=operator.itemgetter(1))[0]

t = Solution()
print(t.majorityElement([1, 2, 1, 1]))
print(t.majorityElement([1, 2, 1, 3, 1, 3]))
