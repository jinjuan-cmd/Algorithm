#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
# 1. dfs/backtraking

# @lc code=start
DIRECTIONS=[(0,-1), (1, 0), (0, 1), (-1,0)]
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== word[0]:
                    visited= set([(i,j)]) # Everytime we look for the first char, we start from it. Also note to set the list not tupple.

                    res = self.dfs(i, j, board, word, 0, visited)
                    if res==True: # return the dfs result. If ommit this one, it will continue to look for other word, until end.
                        return True
        return False

    def dfs(self, x, y, board, word,index, visited):
        if index == len(word)-1:
            return True
        for d_x, d_y in DIRECTIONS:
            new_x= x+ d_x
            new_y= y+ d_y
            if not self.inside(board, new_x, new_y) or (new_x, new_y)  in visited \
                or board[new_x][new_y]!= word[index+1]:
                continue           
            visited.add((new_x,new_y))
            temp = self.dfs(new_x, new_y, board, word,index+1, visited)
            visited.remove((new_x,new_y))
            if temp == True:
                return True
        return False
        
    
    def inside(self,board, x, y):
        m= len(board)
        n= len(board[0])
        if  x>=0 and x<m and y>=0 and y<n:
            return True
        return False

# @lc code=end

