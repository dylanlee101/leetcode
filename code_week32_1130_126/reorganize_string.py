'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorganize-string
'''


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""

        reorganizeArray = [""] * length
        eventIndex, oddINdex = 0, 1
        halfLength = length // 2

        for c, count in counts.items():
            while count > 0 and count <= halfLength and oddINdex < length:
                reorganizeArray[oddINdex] = c
                count -= 1
                oddINdex += 2
            while count > 0:
                reorganizeArray[eventIndex] = c
                count -= 1
                eventIndex += 2
        return "".join(reorganizeArray)