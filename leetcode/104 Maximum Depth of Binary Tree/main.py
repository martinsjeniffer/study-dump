"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.

"""

"""
    SOLUTIONS OBSERVATIONS
    to understand the data structure of a binary tree, enter the /data-structures/binary-tree.py file.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)

        return max(l, r)
        
