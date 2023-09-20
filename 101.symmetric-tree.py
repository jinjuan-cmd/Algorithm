#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution1: DFS, check symmetric left and right
# class Solution:
#     def isSymmetric(self, root) -> bool:
#         return self.check(root.left, root.right)

#     def check(self, r1, r2):
#         if r1 == None and r2 == None:
#             return True
#         elif r1 == None or r2 == None:
#             return False
#         elif r1.val != r2.val:
#             return False
#         else:
#             return self.check(r1.left, r2.right) and self.check(r1.right, r2.left)

# Solution2: BFS, use two queue to check the node.      
class Solution:
    def isSymmetric(self, root) -> bool:
        if root.left == None and root.right == None:
            return True
        
        q1 = deque([root.left])
        q2 = deque([root.right])
        
        while q1 and q2:
            r1 = q1.popleft()
            r2 = q2.popleft()

            if r1 == None and r2 == None:
                continue
            elif r1 == None or r2 == None:
                return False
            elif r1.val != r2.val:
                return False
            q1.append(r1.left)
            q2.append(r2.right)
            q1.append(r1.right)
            q2.append(r2.left)
        return True
        


        

# @lc code=end

