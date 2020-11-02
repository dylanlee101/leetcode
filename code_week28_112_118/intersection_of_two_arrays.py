'''
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_set = set(nums1)
        n2_set = set(nums2)
        return [x for x in n1_set if x in n2_set]