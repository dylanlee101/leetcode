'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
'''
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        left, right, start, valid = 0, 0, 0, 0
        length = math.inf

        while (right < len(s)):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d) - 1
        if length == math.inf:
            return ""
        else:
            return s[start:start + length]