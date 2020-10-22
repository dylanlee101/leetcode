'''
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/univalued-binary-tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        self.v = root.val
        def res(root):
            if not root:
                return True
            return root.val == self.v and res(root.left) and res(root.right)
        return res(root)