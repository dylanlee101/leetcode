
def binarySearch(nums,target):
    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right - left) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

nums = [2,4,5,7,9,10]
target = 5
print(binarySearch(nums,target))