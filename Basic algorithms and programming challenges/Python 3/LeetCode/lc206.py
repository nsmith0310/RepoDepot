# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        l = []
        if head==None:return head
        while head!=None:
            l.append(ListNode(head.val))
            head = head.next
            
        l = l[::-1]    
        
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            i+=1
        return l[0]
