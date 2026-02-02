# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root==None: return True
        
        tmp = [root]
        
        for x in tmp:
            
            if x.left!=None:
                tmp.append(x.left)    
                
            if x.right!=None:
                tmp.append(x.right)
                
        for x in tmp:
            mxl = 0
            mxr = 0
            tmp2 = []
            if x.left!=None or x.right!=None:
                if x.left!=None:
                    tmp2.append([x.left,1,"L"])
                    mxl=1
                if x.right!=None:
                    tmp2.append([x.right,1,"R"])
                    mxr = 1
                for y in tmp2:
                    
                    if y[0].left!=None:
                        if y[2]=="L":
                            if y[1]+1>mxl:mxl=y[1]+1
                            tmp2.append([y[0].left,y[1]+1,"L"])
                        elif y[2]=="R":
                            if y[1]+1>mxr:mxr=y[1]+1
                            tmp2.append([y[0].left,y[1]+1,"R"])
                    if y[0].right!=None:
                        if y[2]=="L":
                            if y[1]+1>mxl:mxl=y[1]+1
                            tmp2.append([y[0].right,y[1]+1,"L"])
                        elif y[2]=="R":
                            if y[1]+1>mxr:mxr=y[1]+1
                            tmp2.append([y[0].right,y[1]+1,"R"])
                if abs(mxl-mxr)>1:
                   
                    return False
                
        return True
                        
                        
                
                
                
                
                
                
                
                
                
                
                
                
                
