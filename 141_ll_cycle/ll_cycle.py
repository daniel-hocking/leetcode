'''
Description: Given a linked list, determine if it has a cycle in it.

Written by: Daniel Hocking
Date created: 26/05/2018
https://leetcode.com/problems/linked-list-cycle/description/
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
    def create_ll(self, in_list):
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
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        current = head
        visited = set()
        while current and current.next:
            visited.add(current)
            if current.next in visited:
                return True
            current = current.next
        return False
            
            

def test_has_cycle(ll):
    '''
    >>> test_has_cycle([])
    False
    >>> test_has_cycle([1])
    False
    >>> test_has_cycle([1, 2, 4])
    False
    '''
    sol = Solution()
    ll = sol.create_ll(ll)
    return sol.hasCycle(ll)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
