'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2: return 0

        max_ = max(nums)
        min_ = min(nums)
        max_gap = 0

        each_bucket_len = max(1, (max_ - min_) // (len(nums) - 1))
        buckets = [[] for _ in range((max_ - min_) // each_bucket_len + 1)]

        for i in range(len(nums)):
            loc = (nums[i] - min_) // each_bucket_len
            buckets[loc].append(nums[i])

        prev_max = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and prev_max != float('inf'):
                max_gap = max(max_gap, min(buckets[i]) - prev_max)

            if buckets[i]:
                prev_max = max(buckets[i])

        return max_gap
