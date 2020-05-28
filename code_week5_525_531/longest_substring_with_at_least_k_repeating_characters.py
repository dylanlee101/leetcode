'''
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import defaultdict
        if not s: return 0
        n = len(s)
        max_num = len(set(s))

        def cal(num):
            left,cur,ge_k = 0,0,0
            c = defaultdict(int)
            res = 0
            for right in range(n):
                c[s[right]] += 1
                if c[s[right]] == 1:
                    cur += 1
                if c[s[right]] == k:
                    ge_k += 1
                while cur > num:
                    if c[s[left]] == 1:
                        cur -= 1
                    if c[s[left]] == k:
                        ge_k -= 1
                    c[s[left]] -= 1
                    left += 1
                if ge_k == num:
                    res = max(res,right-left + 1)
            return res
        return max(cal(num) for num in range(1,max_num+1))