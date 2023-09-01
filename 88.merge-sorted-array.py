#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
# 1. Two pointer. One start from the end to input the bigger number, the other start from nums1's end.
#   Compare nums1's end and nums2's end.
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1)==0:
            nums1 = nums2
    
        p1, p2 = m-1, m+n-1
        i= len(nums2)-1
        while i>=0:
            if nums2[i]>=nums1[p1] or p1<0:
                nums1[p2]=nums2[i]
                p2-=1
                i-=1
            else:
                nums1[p2]=nums1[p1]
                p1-=1
                p2-=1
         


               




# @lc code=end

