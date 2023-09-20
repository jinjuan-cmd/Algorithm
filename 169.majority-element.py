#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# 1. Divide and Conquer
# @lc code=start
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:

#         return self.helper(nums, 0, len(nums))[0]


#     def helper(self, nums, left, right):
#         if left+1 == right:
#             return nums[left], 1 # the right will not get
#         mid = (left + right)//2
#         maj_left, count_left = self.helper(nums, left, mid)
#         maj_right, count_right = self.helper(nums,mid, right)

#         if maj_left == maj_right:
#             maj = maj_left
#             extra = count_left + count_right
#         elif count_left> count_right:
#             maj = maj_left
#             extra = count_left- count_right
#         else:
#             maj = maj_right
#             extra = count_right- count_left
#         return maj, extra


#2. There is more than n/2 majority num, use its count to subtract the count that is different from it.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res = 0
        count = 0

        for i in nums:
            if count ==0:
                res = i # this line is important to get the majority num
            if i == res:
                count+=1
            else:
                count-=1
        return res
            


        
        
# @lc code=end

