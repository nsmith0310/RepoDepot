# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
            
        l1 = [[p.val,'null']]
        
        l2 = [[q.val,'null']]
        
        
        tmp = [p]
        
        for x in tmp:
            
            if x.right!=None:
                tmp.append(x.right)
                l1.append([x.right.val,'r'])
            if x.left!=None:
                tmp.append(x.left)
                l1.append([x.left.val,'l'])
           
                
        tmp = [q]
        
        for x in tmp:
            
            if x.right!=None:
                tmp.append(x.right)
                l2.append([x.right.val,'r'])
            if x.left!=None:
                tmp.append(x.left)
                l2.append([x.left.val,'l'])
        
        return l1==l2
    
    
