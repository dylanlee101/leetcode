'''
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        node = []

        def search(root):
            if root:
                search(root.left)
                node.append(root.val)
                search(root.right)

        search(root)
        return node == sorted(set(node))