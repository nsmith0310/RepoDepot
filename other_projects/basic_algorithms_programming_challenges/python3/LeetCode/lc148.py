# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head==None:return head
        l = []
        
        while head!=None:
            l.append([head.val,ListNode(head.val)])
            head = head.next
        
        l.sort(key=lambda x: x[0])
        
        i = 0
        while i<len(l)-1:
            l[i][1].next=l[i+1][1]
            i+=1
        return l[0][1]
