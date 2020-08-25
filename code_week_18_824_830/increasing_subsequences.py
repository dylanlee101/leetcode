'''
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pres = {(nums[0],)}
        for i in nums[1:]:
            pres.update({j+(i,) for j in pres if j[-1] <= i})
            pres.add((i,))
        return list([list(i) for i in pres if len(i) > 1])