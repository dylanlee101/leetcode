

def twoSum(nums,target):
    left,right = 0,len(nums) - 1
    while left < right :
        tmp = nums[left] + nums[right]
        if tmp == target:
            return [left+1,right+1]
        elif tmp < target:
            left += 1
        elif tmp > target:
            right -= 1
    return [-1,-1]

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))