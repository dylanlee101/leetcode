'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

 

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tmp = {}
        for i,n in enumerate(nums):
            if n not in tmp:
                tmp[n] = i
            else:
                if abs(tmp[n] - i) <= k:
                    return True
                else:
                    tmp[n] = i
        return False

