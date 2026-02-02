# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if root==None: return []
        
        tmp = [[root,1,0,-1]]
        count = 0
        
        for x in tmp:
            count+=1
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1,1,count])
                
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1,0,count])
                
        
        tmp.sort(key = lambda x: x[1])
        
        l = [[] for j in range(0,tmp[-1][1])]
        
        final = []
        i = 0
        while i<len(tmp):
            
            l[tmp[i][1]-1].append([tmp[i][0].val,tmp[i][2],tmp[i][3]])
            i+=1
        l = l[::-1]
        
        f = [[] for x in l]
        i = 0
        while i<len(l):
            tmp = l[i]
            left = []
            
            
            for x in tmp:
                
                left.append(x[0])
            final.append(max(left))     
            
            
            
            i+=1
                            
        return final[::-1]

