#!/usr/bin/env python3
#https://leetcode.com/problems/path-sum/#/description

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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        #print('sum: '+str(sum)+' val: '+str(root.val))
        if (not root.left) and (not root.right) and (sum - root.val == 0):
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    
    def createTest(self, sum):
        b_tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5, None, None), None), None), TreeNode(3, None, None))
        print(self.hasPathSum(b_tree, sum))

t = Solution()
t.createTest(12)
t.createTest(2)
t.createTest(3)
t.createTest(4)
