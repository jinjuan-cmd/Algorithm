#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# Dynamic Programming, however the recurrion method has big time complexity
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        if n == 1:
            return n1
        if n==2: 
            return n2
        
        for i in range(3,n+1):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        return n2

        
# @lc code=end

