'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = s = nums[0]

        for i in range(1, len(nums)):
            t = nums[i]

            if t > 0:
                b, s = max(t, b * t), min(t, s * t)
            else:
                b, s = max(t, s * t), min(t, b * t)

            a = b if b > a else a

        return a