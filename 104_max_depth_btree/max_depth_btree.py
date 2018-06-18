'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
eg.
Input: [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: depth = 3.

Written by: Daniel Hocking
Date created: 26/05/2018
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _maxDepth(self, node):
        if node.left is None and node.right is None:
            return 1
        depth_left = depth_right = 0
        if node.left:
            depth_left = self._maxDepth(node.left)
        if node.right:
            depth_right = self._maxDepth(node.right)
        return max((depth_left, depth_right)) + 1
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self._maxDepth(root)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
