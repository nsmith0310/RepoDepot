# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root==None: return 0
        
        
        tmp = [[root,0,""]]
        
        for x in tmp:
            
            if x[0].left!=None:
                
                if x[2]=="R":
                    tmp.append([x[0].left,x[1]+1,"L"])
                else:
                    tmp.append([x[0].left,0,"L"])
                    
            if x[0].right!=None:
                
                if x[2]=="L":
                    tmp.append([x[0].right,x[1]+1,"R"])
                else:
                    tmp.append([x[0].right,0,"R"])
        tmp.sort(key=lambda x: x[1])
        if len(tmp)==1: return 0
        return tmp[-1][1]+1
