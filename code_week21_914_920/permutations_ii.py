'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,size,depth,path,used,res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums,size,depth+1,path,used,res)
                    used[i] = False
                    path.pop()
        size = len(nums)
        if size == 0:
            return []
        nums.sort()
        used = [False] * len(nums)
        res = []
        dfs(nums,size,0,[],used,res)
        return res