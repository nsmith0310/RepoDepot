# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root==None: return 0
        
        s = 0
        tmp = [root]
        
        for x in tmp:
            if x.val!=None:
                if x.val>=L and x.val<=R:s+=x.val
                
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
                
        return s
