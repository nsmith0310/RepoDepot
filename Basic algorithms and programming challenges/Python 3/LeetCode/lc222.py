# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root==None: return 0
        
        
        l = []
        
        tmp = [root]
        c=1
        for x in tmp:
            
            if x.left!=None:
                c+=1
                tmp.append(x.left)
            if x.right!=None:
                c+=1
                tmp.append(x.right)
        return c
