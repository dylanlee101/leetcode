'''
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-maximum-number
'''
class Solution:
    # 从nums中选取m个数能构成的最大的数字(数的相对位置不变)
    def max_one(self, nums: List[int], m: int):
        n = len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and n-i+len(stack) > m and num > stack[-1]:
                stack.pop()
            stack.append(num)
            if len(stack) > m:
                stack.pop()
        return stack

    def merge(self, arr1: List[int], arr2: List[int]):
        res = []
        while arr1 and arr2:
            if arr1 > arr2:
                res.append(arr1.pop(0))
            else:
                res.append(arr2.pop(0))
        res += arr1 + arr2
        return res

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []
        for i in range(k+1):
            if i > len(nums1) or k-i > len(nums2):
                continue
            arr1 = self.max_one(nums1, i)
            arr2 = self.max_one(nums2, k-i)
            ans = max(ans, self.merge(arr1, arr2))
        return ans
