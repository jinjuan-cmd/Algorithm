#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# 1. For permutation, we need a list to record if the elements in the nums are visited. Also, we need note the backtracking.

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<1:
            return None
        permutations = []
        visited = [False]*len(nums)
        self.dfs(nums, [], permutations, visited)
        return permutations



    def dfs(self, nums, permutation, permutations, visited):
        if len(permutation)==len(nums):
            permutations.append(permutation.copy())

            return

        for i in range(len(nums)):
            if visited[i]==True:
                continue
            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, permutation, permutations,visited)
            visited[i] = False
            permutation.pop()
            
        
# @lc code=end

