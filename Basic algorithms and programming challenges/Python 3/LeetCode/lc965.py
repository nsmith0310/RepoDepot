# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        l = []
        
        tmp = [root]
        
        for x in tmp:
            
            l.append(x.val)
            if x.right!=None:
                tmp.append(x.right)
            if x.left!=None:
                tmp.append(x.left)
        
        if len(list(set(l)))==1:return True
                
