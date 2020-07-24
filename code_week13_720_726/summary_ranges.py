'''
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if not nums:
        #     return []
        # summary = []
        # i = 0
        # while i < len(nums) -1:
        #     tmp_p = i
        #     while i < len(nums) -1 and nums[i] + 1 == nums[i+1] :
        #         i += 1
        #         continue
        #     if tmp_p != i:
        #         summary.append(str(nums[tmp_p])+"->"+str(nums[i]))
        #     else:
        #         summary.append(str(nums[i]))

        #     i += 1
        # if nums[len(nums) -1] != nums[len(nums) -2]+1:
        #         summary.append(str(nums[len(nums) -1]))
        # return summary

        res = []
        if len(nums) == 0: return res

        # 末尾添加一个不连续的数，这样每个原数组元素都能“结算”
        nums.append(nums[0] - 1)

        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                end = nums[i]
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = end = nums[i]
        return res