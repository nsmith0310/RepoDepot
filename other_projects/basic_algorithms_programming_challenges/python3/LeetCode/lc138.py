"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head==None:return head
        
        c = 0
        
        l = []
        m = []
        nodes = []
        ind = []
        while head!=None:
            l.append(Node(head.val))
            m.append(head)
            if head!=None:
                nodes.append(head.random)
            else:
                nodes.append(None)
            
            head = head.next
        m.append(None)
        l.append(None)
        i = 0
        while i<len(nodes):
            ###print(nodes[i])
            ind.append(m.index(nodes[i]))
            i+=1
        
        
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            
            l[i].random = l[ind[i]]
            i+=1
        return l[0]
            
