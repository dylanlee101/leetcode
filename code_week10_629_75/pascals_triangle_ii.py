'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1 for _ in range(rowIndex+1)]
        for i in range(rowIndex + 1):
            for j in range(i-1,0,-1):
                row[j] = row[j] + row[j-1]
        return row