# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root==None: return []
        
        
        
        f = []
        
        
        tmp = [[root,0,[]]]
        
        for x in tmp:
            if x[0]!=None:
                
                if x[0].left==None and x[0].right==None:
                    
                    if x[1]+x[0].val==sum:
                        x[2].append(x[0].val)
                        f.append(x[2])
                
                
                t = [x[0].left,x[1]+x[0].val]
                tmp2 = [y for y in x[2]]
                tmp2.append(x[0].val)
                
                t.append(tmp2)
                tmp.append(t)
                
            
                t = [x[0].right,x[1]+x[0].val]
                tmp2 = [y for y in x[2]]
                tmp2.append(x[0].val)
                
                t.append(tmp2)
                tmp.append(t)
        return f
