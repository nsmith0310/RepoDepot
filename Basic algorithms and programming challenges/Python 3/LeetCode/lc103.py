# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:return root
        
        
        
        tmp = [[root,1,0,-1]]
        count = 0
        o = [root.val]
        for x in tmp:
            count+=1
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1,1,count])
                o.append(x[0].right.val)
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1,0,count])
                o.append(x[0].left.val)
        
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
        while i<len(l):
            tmp = l[i]
            left = []
            
            
            for x in tmp:
                
                left.append([x[0],x[2]])
                
            
            left.sort(key=lambda x: x[1])
            
            left = left[::-1]
            
            
            for y in left:
                f[i].append(y[0])
            
            i+=1
        f = f[::-1]
        i = 0
        while i<len(f):
            if i%2!=0:
                f[i]=f[i][::-1]
            i+=1
        return f
