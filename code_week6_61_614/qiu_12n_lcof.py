'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
'''
class Solution:

    def helper(self,a,b):
        ans = b and self.helper(a << 1,b>>1)
        ans += b & 1 and a
        return ans

    def sumNums(self, n: int) -> int:
        return self.helper(n,n+1) >> 1
