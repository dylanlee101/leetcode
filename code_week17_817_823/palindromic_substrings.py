'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(s,l,r):
            num = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                num += 1
            return num
        num = 0
        for i in range(len(s)):
            num += check(s,i,i)
            if i == len(s) - 1:
                continue
            num += check(s,i,i+1)
        return num