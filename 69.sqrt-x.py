#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# 1. Binary search. Note the condition that exit the iteration left+1< right
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<0:
            return None
        if x==0 or x==1:
            return x
        left, right= 1, x
        while left+1<right:
            mid = (left+ right)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                right = mid
            else:
                left = mid
        return left





        
# @lc code=end