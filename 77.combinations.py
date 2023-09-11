#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# 1. backtracking/dfs. note store the combo
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        combinations = []
        self.dfs(n, k, [], combinations, 1)
        return combinations


    def dfs(self, n, k, combo, combinations, start):
        if len(combo) == k:
            combinations.append(combo.copy())
            return 
        for i in range(start, n+1):
            combo.append(i)
            self.dfs(n, k, combo, combinations, i+1)
            combo.pop()


        
# @lc code=end

