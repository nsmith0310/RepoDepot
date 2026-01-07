# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l = []
        
        
        tmp = [root]
        
        for x in tmp:
            if x!=None:l.append(x.val)
            if x.left!=None:tmp.append(x.left)
            if x.right!=None:tmp.append(x.right)
                
        mn = 10**32 + 1
        
        i = 0
        while i<len(l)-1:
            j = i+1
            while j<len(l):
                if abs(l[i]-l[j])<mn:
                    mn = abs(l[i]-l[j])
                j+=1
            i+=1
        return mn
            
