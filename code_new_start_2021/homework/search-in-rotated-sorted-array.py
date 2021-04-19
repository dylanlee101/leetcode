

class Solution:
    def search(self,nums,target):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[0] <= nums[mid] and (target > nums[mid] or target < nums[0]):
                lo = mid + 1
            elif target > nums[mid] and target < nums[0]:
                lo = mid + 1
            else:
                hi = mid

        return lo == hi and nums[lo] == target if lo else -1
