'''
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def compute_depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx, d, node):
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self.compute_depth(root)
        if d == 0:
            return 1

        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2 ** d - 1) + left

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0


