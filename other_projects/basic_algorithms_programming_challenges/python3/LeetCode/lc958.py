# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        l = []
        
        tmp = [root]
        
        for x in tmp:
            if x==None:
                l.append("*")
            else:
                l.append(str(x.val))
                tmp.append(x.left)
                tmp.append(x.right)
        i = len(l)-1
        while i>=0 and l[i]=="*":
            if l[i]=="*":
                del l[i]
            i-=1
        
        return not "*" in l
