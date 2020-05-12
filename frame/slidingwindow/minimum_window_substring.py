'''
给你一个字符串s，一个字符串t，请在字符串s里面找出：包含t所有字母的最小字符串
输入：s = 'adobecodebanc' t = 'abc'
输出：'banc'
'''
import math


def minWindow(s, t):
    need = {}
    window = {}
    for i in t:
        need[i] = need.get(i, 0) + 1

    left, right, valid = 0, 0, 0
    start, length = 0, math.inf
    while (right < len(s)):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if (window[c] == need[c]):
                valid += 1
        while valid == len(need):
            if (right - left) < length:
                start = left
                length = right - left
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return "" if length == math.inf else s[start:start + length]


s = 'adobecodebanc'
t = 'abc'
print(minWindow(s, t))
