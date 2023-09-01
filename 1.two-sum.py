#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
#1. Brute Force
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         if len(nums)<2 or nums is None:
#             return None
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return i, j


# 2. pass hash table. Note: the one and the compliment are not same.              
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         if len(nums)<2 or nums is None:
#             return None
#         index_table = {}
#         for i in range(len(nums)):
#             index_table[nums[i]] = i
#         for i in range(len(nums)):
#             if (target - nums[i]) in index_table and i != index_table[(target - nums[i])]:
#                 return i, index_table[(target - nums[i])]
            

# 3. one pass hashtable, when put them into talbe and look back to look for matching
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums)<2 or nums is None:
            return None
        index_table = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in index_table:
                return [index_table[compliment], i]
            index_table[nums[i]]=i
            
            


# @lc code=end

