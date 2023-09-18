#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for char in s:
            p = self.findPosition(char, start, t)
            print(p)
            if p is not None:
                start = p+1
            else:
                return False
        return True
        


    def findPosition(self, char, start, t):
        for i in range(start, len(t)):
            if t[i]== char:
                return i
        return None
        

        
# @lc code=end

