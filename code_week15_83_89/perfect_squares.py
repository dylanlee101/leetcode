'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
'''
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(0,int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i],dp[i-square] + 1)
        return dp[-1]