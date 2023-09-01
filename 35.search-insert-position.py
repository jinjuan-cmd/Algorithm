#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start

# 1. Ordered and time complexity is logn. Binary search is a good choice.
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right =0 , len(nums)-1
        if target< nums[left]:
            return 0
        if target> nums[right]:
            return right+1
        
        while left+1<right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right= mid
            else:
                left = mid
        if target > nums[left] and target < nums[right] :
            return left+1
        elif target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        
         
        
# @lc code=end

