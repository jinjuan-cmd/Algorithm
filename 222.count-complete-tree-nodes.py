#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self.depth(root)

        if d ==0:
            return 1

        # searchLastNode
        start, end = 1, 2**d-1
        while start<= end:
            pivot = (start + end)//2
            print(start, end, pivot)
            #print(self.Exist(root, d, pivot))
            if self.Exist(root, d, pivot):
                start = pivot + 1
            else:
                end = pivot -1
        return start + 2**d-1

        

    def depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d
    
    def Exist(self, node, d, idx):
        left, right = 0, 2**d-1
        while left< right:
            mid = (left+right)//2
            # print(idx, mid)
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid+1
        return node is not None
    

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

# example = Solution()
# print(example.countNodes(root))




# @lc code=end

