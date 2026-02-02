# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root==None: return 0
        
        
        
        tmp = [[root,1]]
        
        
        for x in tmp:
            
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1])
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1])
                
        tmp.sort(key = lambda x: x[1])
        
        l = [0 for j in range(0,tmp[-1][1])]
        
        
        i = 0
        while i<len(tmp):
            
            l[tmp[i][1]-1]+=tmp[i][0].val
            i+=1
        num = max(l)
        return l.index(num)+1
