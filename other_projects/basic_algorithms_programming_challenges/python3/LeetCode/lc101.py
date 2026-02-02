# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root==None:return True
        
        tmp = [[root,1,0,-1,1]]
        count = 0
        
        for x in tmp:
            count+=1
            if x[4]==1:
                if x[0].right!=None:
                    tmp.append([x[0].right,x[1]+1,1,count,1])
                else:
                    tmp.append([TreeNode(-99),x[1]+1,1,count,0])
                if x[0].left!=None:
                    tmp.append([x[0].left,x[1]+1,0,count,1])
                else:
                    tmp.append([TreeNode(-99),x[1]+1,0,count,0])
                
        
        tmp.sort(key = lambda x: x[1])
        
        l = [[] for j in range(0,tmp[-1][1])]
        
        
        i = 0
        while i<len(tmp):
            
            l[tmp[i][1]-1].append([tmp[i][0].val,tmp[i][2],tmp[i][3]])
            i+=1
        l = l[::-1]
        ###print(l)
        f = [[] for x in l]
        i = 0
        while i<len(l)-1:
            tmp = l[i]
            left = []
            right = []
            
            for x in tmp:
                if x[1]==0:
                    left.append(x[0])
                else:
                    right.append(x[0])
           
            
            if left!=right[::-1]:
                return False
            
            
            i+=1
                            
        return True
