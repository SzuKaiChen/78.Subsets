# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#solution from Chih-Yu Lin@medium

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return 
        l, r = root.left, root.right
        self.flatten(root.left)
        self.flatten(root.right)
        root.left = None
        root.right = l
        while root.right:
            root = root.right
        root.right = r
        
