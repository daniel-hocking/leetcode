'''
Description: Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.
eg.
Input: [0,0,1,1,1,2,2,3,3,4]
Output: 5
and array = [0, 1, 2, 3, 4]

Written by: Daniel Hocking
Date created: 26/05/2018
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        original_len = len(nums)
        if original_len < 2:
            return original_len
        pointer = 0
        for i in range(1, original_len):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1

    '''
    Too slow, times out on last test case
    '''
    def removeDuplicatesOld(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        original_len = current_len = len(nums)
        if original_len < 2:
            return original_len
        pointer = 0
        while pointer < (current_len - 1):
            if nums[pointer] == nums[pointer + 1]:
                current_len -= 1
                prev_num = nums[pointer + 1]
                for i in range(current_len, pointer, -1):
                    nums[i], prev_num = prev_num, nums[i]
            else:
                pointer += 1
        return current_len
        
            

def test_remove_duplicates(nums):
    '''
    >>> test_remove_duplicates([])
    (0, [])
    >>> test_remove_duplicates([1, 2])
    (2, [1, 2])
    >>> test_remove_duplicates([1, 2, 2, 4])
    (3, [1, 2, 4])
    >>> test_remove_duplicates([1, 1, 1, 1, 2, 2, 4])
    (3, [1, 2, 4])
    >>> test_remove_duplicates([0,0,1,1,1,2,2,3,3,4])
    (5, [0, 1, 2, 3, 4])
    '''
    sol = Solution()
    num = sol.removeDuplicates(nums)
    return num, nums[:num:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
