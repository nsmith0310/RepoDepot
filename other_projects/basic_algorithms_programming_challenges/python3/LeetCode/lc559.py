"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0

        l = [[root,0]]

        c = 1

        c2 = len(root.children)

        tmp = 0
        while l!=[]:
            y = l.pop()
            f = y[1]+1

            for x in y[0].children:
                c2-=1
                tmp +=len(x.children) 
                l.insert(0,[x,c])

            if c2==0:
                c2 = tmp
                tmp = 0
                c+=1
                
        return f
        
            
