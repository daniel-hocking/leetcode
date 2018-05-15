# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution:
    def mergeTwoLists(self, l1, l2):
        pre = tmp = None
        cur = l1
        while cur and cur.next:
            if cur.val > l2.val:
                tmp = cur
                cur = l2
                if pre:
                    pre.next = cur
                cur.next = tmp
                l2 = l2.next
                if not l2:
                    break
            cur = cur.next
        if l2:
            cur.next = l2
        return l1

    def createTestA(self):
        l1 = ListNode(1, ListNode(2, ListNode(4, None)))
        l2 = ListNode(1, ListNode(3, ListNode(4, None)))
        print(self.mergeTwoLists(l1, l2))

t = Solution()
t.createTestA()
                
