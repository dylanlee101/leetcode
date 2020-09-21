'''
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
'''


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left = 0
        right = len(words)
        while left < right:
            mid = left + (right - left) // 2
            if words[mid] == "" and words[left] != s:
                left += 1
                continue
            elif words[left] == s:
                return left

            if words[mid] == s:
                return mid
            elif words[mid] > s:
                right = mid
            elif words[mid] < s:
                left = mid + 1
        return -1