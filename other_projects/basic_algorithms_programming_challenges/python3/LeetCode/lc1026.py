# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        if root==None: return 0
        
        
        tmp = [root]
        
        for x in tmp:
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
                
                
        mx = -9999999999999
        
        for x in tmp:
            tmp2 = [x]
            for y in tmp2:
                if abs(y.val-x.val)>mx:
                    mx=abs(y.val-x.val)
                if y.right!=None:
                    tmp2.append(y.right)
                if y.left!=None:
                    tmp2.append(y.left)
        return mx
