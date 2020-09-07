'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_dict = {}
        for n in nums:
            if n not in top_dict:
                top_dict[n] = 1
            else:
                top_dict[n] += 1
        results = []
        # print(top_dict)
        for ke,v in sorted(top_dict.items(),key = lambda x:x[1],reverse=True):
            results.append(ke)
        # print(results)
        return results[:k]