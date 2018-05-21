'''
Description: Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first
two lists.
eg.
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Written by: Daniel Hocking
Date created: 21/05/2018
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create_ll(seld, in_list):
        len_list = len(in_list)
        if not len_list:
            return None
        head = ListNode(in_list[0])
        current = head
        for i in range(1, len_list):
            current.next = ListNode(in_list[i])
            current = current.next
        return head

    def ll_to_list(self, ll):
        if not ll:
            return []
        l = []
        while ll:
            l.append(ll.val)
            ll = ll.next
        return l
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if (l1 and l2 and l1.val < l2.val) or \
           (l1 and not l2):
            head = l1
            l1 = l1.next
        elif l2:
            head = l2
            l2 = l2.next
        else:
            return None
        current = head
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 is not None:
            current.next = l1
        else:
            current.next = l2
        return head
            

def test_merge_two_lists(l1, l2):
    '''
    >>> test_merge_two_lists([], [])
    []
    >>> test_merge_two_lists([1], [2])
    [1, 2]
    >>> test_merge_two_lists([1, 2, 4], [1, 3, 4])
    [1, 1, 2, 3, 4, 4]
    '''
    sol = Solution()
    ll_1 = sol.create_ll(l1)
    ll_2 = sol.create_ll(l2)
    ll = sol.mergeTwoLists(ll_1, ll_2)
    return sol.ll_to_list(ll)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
