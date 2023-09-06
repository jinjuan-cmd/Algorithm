#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#Trick:  reverse the thinking. We iterate the time and count the bit. Use recursion to count the binary bit.

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if turnedOn>=9:
            return []
        res = []
        for i in range(12):
            for j in range(60):
                if self.DecimaltoBinaryCount(i, [])+self.DecimaltoBinaryCount(j, []) == turnedOn:
                    res.append(str(i)+':'+ str(j).zfill(2))
        return res
                

        
    
    def DecimaltoBinaryCount(self, num: int, bit):
        if num >=1:
            self.DecimaltoBinaryCount( num//2, bit)
            bit.append(num%2)
        return sum(bit)



        
# @lc code=end

