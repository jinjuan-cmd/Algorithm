#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

# 1. two pointer
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left, right = 0, 1
        while right <len(nums):
            if nums[right]!=nums[left]:
                left+=1
                nums[left]=nums[right]
            right+=1
        for i in range(left+1, len(nums)):
            nums[i]= '_'
        return left+1
            

            


        
# @lc code=end

