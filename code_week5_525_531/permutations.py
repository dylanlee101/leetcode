'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])

            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res