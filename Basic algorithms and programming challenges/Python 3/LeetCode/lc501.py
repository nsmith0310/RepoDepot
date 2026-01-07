# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root==None:return []
        k = set()
        l = []
        mx = -9999999999999999
        
        
        tmp = [root]
        
        for x in tmp:
            if x.val!=None:
                l.append(x.val)
                k.add(x.val)
            if x.right!=None:
                tmp.append(x.right)
            if x.left!=None:
                tmp.append(x.left)
        
        
        
        k1 = list(k)
        for x in k1:
            if l.count(x)>mx:
                mx = l.count(x)
        
        final=[]
        for x in k1:
            if l.count(x)==mx:
                
                final.append(x)
        return final
