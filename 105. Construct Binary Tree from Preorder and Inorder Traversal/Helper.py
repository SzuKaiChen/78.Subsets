class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        
        def helper(preorder, inorder, pre_st, in_st, in_end):
            if (pre_st > len(preorder) or in_st > in_end):
                return None
            res = TreeNode(preorder[pre_st])
            i = in_st
            while (i <= in_end):
                if (inorder[i] == preorder[pre_st]):
                    break
                i += 1
            
            res.left = helper(preorder, inorder, pre_st + 1, in_st, i-1)
            res.right = helper(preorder, inorder, pre_st +(i -in_st +1), i+1, in_end)
            return res
        
        return helper(preorder, inorder, 0, 0, len(preorder) - 1)
