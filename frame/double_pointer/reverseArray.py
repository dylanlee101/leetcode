
def reverseArray(nums):
    left,right = 0,len(nums) - 1
    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp

        left += 1
        right -= 1

nums = [2,3,4,5,6]
reverseArray(nums)
print(nums)