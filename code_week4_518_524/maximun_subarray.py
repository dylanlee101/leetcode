'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_v = nums[0]
        sum_v = 0
        for i in range(len(nums)):

            if sum_v > 0:
                sum_v += nums[i]
            else:
                sum_v = nums[i]
            max_v = max(sum_v, max_v)
        return max_v
