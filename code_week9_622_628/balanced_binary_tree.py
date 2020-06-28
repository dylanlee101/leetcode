'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isBalancedHelper(self,root):
        if not root:
            return True,-1
        leftIsBalanced,leftHight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False,0
        rightIsBalaced,rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalaced:
            return False,0
        return (abs(leftHight - rightHeight) < 2),1+max(leftHight,rightHeight)



    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
