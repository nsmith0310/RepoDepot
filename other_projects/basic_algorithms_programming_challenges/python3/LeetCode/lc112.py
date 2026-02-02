# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False    
        
        tmp = [[root,0]]
        
        
        for x in tmp:
            
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+x[0].val])
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+x[0].val])
                
                
        
        for x in tmp:
            if x[0].left==None and x[0].right==None:
                x[1]+=x[0].val
                
        for x in tmp:
            if x[1]==sum: 
                if x[0]==root:
                    if root.val==sum and len(tmp)==1:
                    
                        return True
                else:
                    if x[0].left==None and x[0].right==None:
                        return True
            
            
            
        return False
