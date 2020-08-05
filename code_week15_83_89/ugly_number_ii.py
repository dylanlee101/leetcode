'''
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
'''
class Ugly:
    def __init__(self):
        self.nums = nums = [1,]
        i2 = i3 = i5 = 0

        for i in range(1,1690):
            ugly = min(nums[i2] * 2,nums[i3] * 3,nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1


class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]