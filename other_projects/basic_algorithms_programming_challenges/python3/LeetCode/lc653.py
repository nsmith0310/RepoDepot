# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        if root==None:return False
        
        l = []
        
        tmp = [root]
        
        for x in tmp:
            l.append(x.val)
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
                
        i = 0
        while i<len(l):
            if k-l[i] in l and l.index(k-l[i])!=i:return True
            i+=1
        return False
