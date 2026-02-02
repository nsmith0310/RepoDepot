# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        v=x
        tmp = [[root,1,None]]
        
        
        for x in tmp:
            
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1,x[0].val])
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1,x[0].val])
                
        tmp.sort(key = lambda x: x[1])
        
        d1 = [-1,-1]
        d2 = [-1,-1]
        
        i = 0
        while i<len(tmp):
            if tmp[i][0].val==v:
                d1[0]=tmp[i][1]
                d1[1]=tmp[i][2]
            if tmp[i][0].val==y:
                d2[0]=tmp[i][1]
                d2[1]=tmp[i][2]
            i+=1
        
        if d1[0]==d2[0] and d1[1]!=d2[1]:
            return True
        else:
            return False
        
                
