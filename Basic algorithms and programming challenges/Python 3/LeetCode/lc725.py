# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from math import ceil

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        
        if root==None: return [None for x in range(0,k)]
        
        l = []
        
        
        c = 0
        while root!=None:
            l.append(ListNode(root.val))
            c+=1
            root=root.next
            
        if c==k:
            return [x for x in l]
        elif c<k:
            tmp = [x for x in l]
            while c<k:
                tmp.append(None)
                c+=1
            return tmp
        else:

            f = []
            while l!=[]:
                tmp = []
                length = ceil(c/k)
                
                while len(tmp)<length:
                    tmp.append(l[0])
                    del l[0]
                
                i = 0
                while i<len(tmp)-1:
                    tmp[i].next = tmp[i+1]
                    i+=1
                
                f.append(tmp[0])
                c-=length
                k-=1
            return f
            
        
        
