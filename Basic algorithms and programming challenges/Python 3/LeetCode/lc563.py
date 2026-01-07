# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root==None: return 0
        if root.left==None and root.right==None: return 0
        
        total = 0
        
        tmp = [root]
        
        for x in tmp:
            
            left = 0
            right = 0
            
            l = []
            r = []
            
            if x.left!=None: 
                l.append(x.left)
                tmp.append(x.left)
                ###print(x,1)
            if x.right!=None: 
                r.append(x.right)
                tmp.append(x.right)
                ###print(x,2)
                
            for y in l:
                left+=y.val
                if y.left!=None:
                    l.append(y.left)
                if y.right!=None:
                    l.append(y.right)
                    
            for z in r:
                right+=z.val
                if z.left!=None:
                    r.append(z.left)
                if z.right!=None:
                    r.append(z.right)
                    
            total+=abs(left-right)
            
        return total
            
            
            
            
            
            
            
            
            
            
            
            
            
            
