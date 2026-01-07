# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if root==None:return 0
        
        
        s = 0
        
        tmp = [root]
        
        for x in tmp:
            if x.left!=None:
                if x.left.left==None and x.left.right==None:
                    s+=x.left.val
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
        return s
