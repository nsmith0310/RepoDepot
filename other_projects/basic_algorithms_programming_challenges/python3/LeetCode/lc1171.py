# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head==None:return head
        l = []
        
        while head!=None:
            l.append(head.val)
            head = head.next
            
        
        i = 0
        while i<len(l)-1:
            j = len(l)
            while j>=i:
                if sum(l[i:j])==0:
                    del l[i:j]
                    
                j-=1
            i+=1
        while 0 in l:
            del l[l.index(0)]
        if l==[]:
            tmp = ListNode()
            tmp = tmp.next
            return tmp
            
        f = [ListNode(x) for x in l]
        i = 0
        while i<len(f)-1:
            f[i].next = f[i+1]
            i+=1
        
        return f[0]
            
