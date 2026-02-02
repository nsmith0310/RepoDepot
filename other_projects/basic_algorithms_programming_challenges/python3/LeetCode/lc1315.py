# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        tmp = [root]
        
        t = 0
        
        for x in tmp:
            if x.left!=None:
                tmp.append(x.left)
                if x.left.left!=None: 
                    if x.val%2==0:
                        t+=x.left.left.val
                if x.left.right!=None: 
                    if x.val%2==0:
                        t+=x.left.right.val
            if x.right!=None:
                tmp.append(x.right)
                if x.right.left!=None: 
                    if x.val%2==0:
                        t+=x.right.left.val
                if x.right.right!=None: 
                    if x.val%2==0:
                        t+=x.right.right.val
                        
        return t
