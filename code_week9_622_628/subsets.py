'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        output = [[]]

        for num in nums:
            output += [cur + [num] for cur in output]
        return output