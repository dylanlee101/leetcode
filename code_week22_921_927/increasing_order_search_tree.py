'''
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

 

示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-order-search-tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        Tree = []

        def create_new_tree(temp):
            if temp.left: create_new_tree(temp.left)
            new_node = TreeNode(temp.val)
            Tree.append(new_node)
            if temp.right: create_new_tree(temp.right)

        create_new_tree(root)
        new_root = Tree[0]
        for i in Tree[1:]:
            new_root.right = i
            new_root = i
        return Tree[0]

