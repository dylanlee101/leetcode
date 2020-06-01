'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        for l in range(len(s)):
            if i < j and s[i] == s[j]:
                i += 1
                j -= 1
        return self.palindrome(s,i,j-1) or self.palindrome(s,i+1,j)

    def palindrome(self,s,i,j):
        for l in range(len(s)):
            if i < j and s[i] == s[j]:
                i += 1
                j -= 1
        return i >= j