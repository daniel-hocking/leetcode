'''
Description: Given an array nums and a value val, remove all instances of
that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.
eg.
Input: [3,2,2,3], val = 3
Output: 2
and array = [2, 2]

Written by: Daniel Hocking
Date created: 26/05/2018
https://leetcode.com/problems/remove-element/description/
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        original_len = len(nums)
        if not original_len:
            return original_len
        pointer = 0
        for i in range(1, original_len):
            if nums[pointer] == val:
                nums[pointer], nums[i] = nums[i], nums[pointer]
            if nums[pointer] != val:
                pointer += 1
        return pointer + (1 if nums[pointer] != val else 0)
        
            

def test_remove_element(nums, val):
    '''
    >>> test_remove_element([], 0)
    (0, [])
    >>> test_remove_element([1, 2], 3)
    (2, [1, 2])
    >>> test_remove_element([1, 2, 2, 4], 4)
    (3, [1, 2, 2])
    >>> test_remove_element([1, 1, 1, 1, 2, 2, 4], 1)
    (3, [2, 2, 4])
    >>> test_remove_element([0,0,1,1,1,2,2,3,3,4], 3)
    (8, [0, 0, 1, 1, 1, 2, 2, 4])
    >>> test_remove_element([3, 2, 2, 3], 3)
    (2, [2, 2])
    '''
    sol = Solution()
    num = sol.removeElement(nums, val)
    return num, nums[:num:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
