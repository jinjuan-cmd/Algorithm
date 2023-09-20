#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
# 1. BFS, To do this a queue is used. All the adjacent unvisited nodes of the
#   current level are pushed into the queue and the nodes of the current level 
#  are marked visited and popped from the queue.

# DIRECTION = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# from collections import deque

# class Solution:
#     def numIslands(self, grid: list[list[str]]) -> int:
#         visited = set()
#         q = deque()
#         res = 0
#         count =0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if self.island(grid, i, j) and (i,j) not in visited:
#                     count+=1
#                     q.append((i, j))
#                     visited.add((i,j))
#                     self.BFS(grid, q, visited)
#                     res+=1
#         return res
    
#     def BFS(self, grid, q, visited):

#         while q:
#             cur = q.popleft()
#             for d_x, d_y in DIRECTION:
#                 new_x = cur[0] + d_x
#                 new_y = cur[1] + d_y
#                 if self.island(grid, new_x, new_y) and (new_x, new_y) not in visited:
#                     q.append((new_x, new_y))
#                     visited.add((new_x, new_y))
            

#     def island(self, grid, x, y):
#         m, n = len(grid), len(grid[0])
#         if 0 <= x <m and 0 <= y <n and grid[x][y]=='1':
#             return True
#         else:
#             return False 


# 2. DFS
DIRECTION = [(0, -1), (1, 0), (0, 1), (-1, 0)]

from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.island(grid, i, j) and (i,j) not in visited:
                    self.DFS(grid, i, j, visited)
                    res+=1
        return res
    
    def DFS(self, grid, i, j, visited):
        for d_x, d_y in DIRECTION:
            new_x = i + d_x
            new_y = j + d_y
            if self.island(grid, new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                self.DFS(grid, new_x, new_y, visited)
            else:
                continue
        return 

               
            

    def island(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        if 0 <= x <m and 0 <= y <n and grid[x][y]=='1':
            return True
        else:
            return False  
        

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
example = Solution()
print(example.numIslands(grid))

# @lc code=end

