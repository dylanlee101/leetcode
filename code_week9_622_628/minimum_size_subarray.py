'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
'''
import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = sys.maxsize
        n = len(nums)

        left = 0
        right = 0
        sum_n = 0

        while right < n:
            sum_n += nums[right]
            right += 1

            while (sum_n >= s):
                ans = min(ans, right - left)
                sum_n -= nums[left]
                left += 1

        if ans != sys.maxsize:
            return ans
        else:
            return 0