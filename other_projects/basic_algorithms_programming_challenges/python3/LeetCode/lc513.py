# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
       
        
        
        
        tmp = [[root,1,0]]
        
        
        for x in tmp:
            
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1,1])
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1,0])
                
        
        tmp2 = [x for x in tmp]
        tmp2.sort(key = lambda x: x[1])
        tmp2 = tmp2[::-1]
       
        mx = tmp2[0][1]
        i = 0
        while i<len(tmp2) and tmp2[i][1]==mx:
            
            return tmp2[i][0].val
            
            
            i+=1
            
