# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root==None: return -1
        
        l=[]
        tmp = [root]
        
        for x in tmp:
            if x.val!=None:
                l.append(x.val)
                
            if x.right!=None:
                tmp.append(x.right)
            if x.left!=None:
                tmp.append(x.left)
        k = list(set(l))   
        k.sort()
        try:
            return k[1]
        except:
            return -1
