#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
# 1. use one variable to store the max length
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if nums is None:
            return None

        curlen = 1
        maxlen = curlen
        cur= nums[0]
        for i in range(1,len(nums)):
            if nums[i]>cur:
                cur = nums[i]
                curlen += 1
                maxlen = max(maxlen, curlen)
            else:
                cur = nums[i]
                curlen =1
            
        return maxlen

            


# @lc code=end

