# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head==None: return head
        
        l = []
        while head!=None:
            l.append(head.val)
            head = head.next
        
        m = list(set(l))
        if len(m)==1:
            return ListNode(m[0])
        m.sort()
        
        f = [ListNode(x) for x in m]
        
        i = 0
        while i<len(f)-1:
            f[i].next = f[i+1]
            i+=1
        return f[0]
