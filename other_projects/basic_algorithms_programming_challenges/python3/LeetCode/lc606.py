# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def r(self,node):
        m = "("
        
        if node!=None:
            m+=str(node.val)
            m+=self.r(node.left)+")"
            m+=self.r(node.right)+")"
        
        return m
    
    def tree2str(self, t: TreeNode) -> str:
        s = self.r(t)
        
        
        while "()()" in s:
            l = list(s)
            ind = s.index("()()")
            del l[ind:ind+4]
            s = ''.join(l)
        
        while ")()" in s:
            l = list(s)
            ind = s.index(")()")
            del l[ind+1:ind+3]
            s = ''.join(l)
        
        
        return s[1:]
    
        
        
