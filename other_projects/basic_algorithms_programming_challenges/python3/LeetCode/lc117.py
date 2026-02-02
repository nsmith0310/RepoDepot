"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:return root
        l = []
        tmp = [[root,1]]
        
        
        for x in tmp:
            l.append([x[0],x[1]])
            
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1])
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1])
        f = [[] for i in range(0,l[-1][1])]
        
        i = 0
        while i<len(l):
            
            f[l[i][1]-1].append(l[i][0])
            i+=1
        
        i = 0
        while i<len(f):
            j = 0
            while j<len(f[i])-1:
                f[i][j].next = f[i][j+1]
                j+=1
            f[i][-1].next = None
            i+=1
        return f[0][0]
