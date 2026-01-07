# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        
        if head==None:return head
        
        e = []
        
        o = []
        
        i = 0
        
        while head!=None:
            if i%2==0:
                e.append(ListNode(head.val))
            else:
                o.append(ListNode(head.val))
            head = head.next
            i+=1
        for x in o:
            e.append(x)
            
        if len(e)==1:
            return e[0]
        
        i = 0
        while i<len(e)-1:
            e[i].next = e[i+1]
            i+=1
        return e[0]
