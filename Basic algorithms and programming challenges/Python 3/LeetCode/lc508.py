# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        
        if root==None:
            return []
        
        f = []
        d = dict()
        mx = 0
        tmp = [root]
        
        for x in tmp:
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
                
        for x in tmp:
            tmp2 = [x]
            s = 0
            for y in tmp2:
                if y!=None:
                    s+=y.val
                    tmp2.append(y.left)
                    tmp2.append(y.right)
            
            try:
                d[s]+=1
                if d[s]>=mx:
                    mx = d[s]
            except:
                d[s]=1
                if d[s]>=mx:
                    mx = d[s]
        
        for x in d:
            
            if d.get(x)==mx:
                
                f.append(x)
        return f
