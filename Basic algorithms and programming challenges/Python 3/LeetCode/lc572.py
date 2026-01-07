# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s==None:
            if t==None:
                return True
            else:
                return False
        
        tmp = [s]
        
        for x in tmp:
            
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
        
        
        for x in tmp:
            if x.val==t.val:
                l1 = []
                l2 = []
                a = [x]
                b = [t]
                for y in a:
                    l1.append(y.val)
                    if y.left!=None:
                        a.append(y.left)
                    if y.right!=None:
                        a.append(y.right)
                for z in b:
                    l2.append(z.val)
                    if z.left!=None:
                        b.append(z.left)
                    if z.right!=None:
                        b.append(z.right)
                if l1==l2:return True
                
        return False
        
        
