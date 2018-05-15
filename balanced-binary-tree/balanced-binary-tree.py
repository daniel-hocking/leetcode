#!/usr/bin/env python3
#https://leetcode.com/problems/balanced-binary-tree/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def depth(self, root):
        if root == None:
            return 0;
        return max(self.depth(root.left), self.depth(root.right)) + 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def createTestA(self):
        b_tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5, None, None), None), None), TreeNode(3, None, None))
        print(self.isBalanced(b_tree))

t = Solution()
t.createTestA()
