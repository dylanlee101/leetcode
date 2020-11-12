'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
'''


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)

        ans = [0] * n
        # 第一次遍历
        # 将偶数放到索引为偶数的位置上
        x = 0
        for i in range(n):
            if A[i] % 2 == 0:
                ans[x] = A[i]
                x += 2
        # 第二次遍历
        # 将奇数放到索引为奇数的位置上
        y = 1
        for j in range(n):
            if A[j] % 2 == 1:
                ans[y] = A[j]
                y += 2

        return ans
