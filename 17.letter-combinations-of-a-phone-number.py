#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# 1. use index to iterate digits. DFS method.
# @lc code=start
keyboard ={'1': None,
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res =[]
        if len(digits)==0:
            return []
        self.AlphaCombo(0, digits, [], res)
        return res

    def AlphaCombo(self, index, digits, combo, res):
        if len(combo) == len(digits):
            res.append(''.join(combo))
            return res
        for char in keyboard[digits[index]]:
            combo.append(char)
            self.AlphaCombo(index+1, digits, combo, res)
            combo.pop()


        
# @lc code=end

