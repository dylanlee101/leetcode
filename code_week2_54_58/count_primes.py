'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
https://leetcode-cn.com/problems/count-primes/
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        results = [1] * n
        results[0],results[1] = 0,1
        for i in range(2,int(n**0.5)+1):
            if results[i] == 1:
                results[i*2:n:i] = [0] * len(results[i*2:n:i])
        return sum(results)-1