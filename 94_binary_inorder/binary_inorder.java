/**
 * Given a binary tree, return the inorder traversal of its nodes' values.
 * 
 * Written by: Daniel Hocking
 * Date created: 31/03/2019
 * https://leetcode.com/problems/binary-tree-inorder-traversal/
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> list = new ArrayList<>();
        TreeNode current = root;
        
        do {
            while(current != null) {
                stack.push(current);
                current = current.left;
            }
            if(stack.empty()) {
                break;
            }
            current = stack.pop();
            list.add(current.val);
            current = current.right;
        } while(current != null || !stack.empty());
        
        return list;
    }
}