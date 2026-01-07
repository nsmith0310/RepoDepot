# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:return head
        
        lim = 0
        l = []
        
        while head!=None:
            l.append(ListNode(head.val))
            lim+=1
            head=head.next
        if lim==1:
            return l[0]
        
        if k==0 or k%lim==0:
            i = 0
            while i<len(l)-1:
                l[i].next=l[i+1]
                i+=1
            return l[0]
        
        ind = k%lim 
        
        m = []
        n = []
        
        i = len(l)-1
        c = 1
        while i>=0:
            if c<=ind:
                m.insert(0,l[i])
            else:
                n.insert(0,l[i])
            c+=1
            i-=1
        
        
        
        
        for x in n:
            m.append(x)
        i = 0
        while i<len(m)-1:
            m[i].next = m[i+1]
            i+=1
        return m[0]
            
        
