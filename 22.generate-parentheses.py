#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n<1:
            return []
        res = []
        self.matchparenthesis(n, '', res, 0, 0)
        return res

    def matchparenthesis(self, n, onematch, res, left, right):
        if left>n or right>n:
            return
        if right>left:
            return 
        if left==n and right==n:
            res.append(''.join(onematch))
            return
        self.matchparenthesis(n, onematch+'(', res, left+1, right)
        self.matchparenthesis(n, onematch+')', res, left, right+1)
        
            


        
# @lc code=end

