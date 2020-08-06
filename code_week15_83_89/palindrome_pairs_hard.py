'''
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]]
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]]
解释: 可拼接成的回文串为 ["battab","tabbat"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def findWord(s,left,right):
            return indices.get(s[left:right+1],-1)

        def isPalindrome(s,left,right):
            return (sub := s[left:right+1]) == sub[::-1]
        n = len(words)
        indices = {word[::-1] : i for i,word in enumerate(words)}
        ret = list()
        for i , word in enumerate(words):
            m = len(word)
            for j in range(m+1):
                if isPalindrome(word,j,m-1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret
