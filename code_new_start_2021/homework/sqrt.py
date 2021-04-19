'''
'''

class Solution:
    def sqrtx(self,x):
        if x== 0 or x == 1:
            return x
        left,right = 1,x

        while left < right:
            mid = left + (right - left) / 2
            if mid * mid > x:
                right = mid -1
            else:
                left = mid + 1

        return int(right)

class Solution2:
    def mySqrt(self,x):
        if x == 0:
            return 0

        cur = x
        while cur * cur > x:

            cur = (cur + x / cur) / 2

        return int(cur)