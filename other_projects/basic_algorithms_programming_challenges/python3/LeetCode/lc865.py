# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        if root==None:return root
        
        
        tmp = [[root,0]]
        tmp2 = [root]
        for x in tmp:
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1])
                tmp2.append(x[0].left)
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1])
                tmp2.append(x[0].right)
                
        tmp.sort(key=lambda x: x[1])
        
        lim = len(tmp)
        if lim==1:
            return tmp[0][0]
        
        tmp = tmp[::-1]
        tmp2 = tmp2[::-1]
        vals = []
        i = 0
        while i<lim:
            if tmp[i+1][1]!=tmp[i][1]:
                vals.append(tmp[i][0])
                break
            else:
                vals.append(tmp[i][0])
            i+=1
        
        for x in tmp2:
            vals2 = [0 for x in range(0,len(vals))]
            tmp2 = [x]
            for y in tmp2:
                if y!=None:
                    if y in vals:
                        vals2[vals.index(y)]=1
                    tmp2.append(y.left)
                    tmp2.append(y.right)
            if list(set(vals2))==[1]:
                return x
            
