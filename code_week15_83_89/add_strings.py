'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1) -1, len(num2) -1
        carry = 0
        res = ""
        while m >=0 or n >= 0:
            n1 = int(num1[m]) if m >=0 else 0  # 可能最高位为空需要补0
            n2 = int(num2[n]) if n >=0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            m -=1
            n -=1
        return "1" + res if carry else res

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def to_int(num_str):
            n_int = 0
            for n in num_str:
                n_int = 10 * n_int + int(n)
            return n_int

        return str((to_int(num1) + to_int(num2)))