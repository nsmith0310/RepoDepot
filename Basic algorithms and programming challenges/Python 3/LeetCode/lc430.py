"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def r(self,head):
        m = []
        
        while head!=None:
            m+=[head.val]
            if head.child!=None:
                m+=self.r(head.child)
            
            head=head.next
        return m
        
    def flatten(self, head: 'Node') -> 'Node':
        l = [Node(x) for x in self.r(head)]
        
        lim = len(l)
        if lim==1:
            return l[0]
        if lim==0:
            return None
        
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            i+=1
        i = lim-1
        while i>=1:
            l[i].prev = l[i-1]
            i-=1
        return l[0]
