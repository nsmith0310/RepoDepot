# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:return []
        l = []
        tmp = [[root,1]]
        
        
        for x in tmp:
            l.append([x[0].val,x[1]])
            
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1])
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1])
        f = [[] for i in range(0,l[-1][1])]
        
        i = 0
        while i<len(l):
            
            f[l[i][1]-1].append(l[i][0])
            i+=1
        return f
