'''
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :



返回其前序遍历: [1,3,5,6,2,4]。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [root, ]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])

        return res

