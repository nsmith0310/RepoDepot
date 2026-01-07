# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        l = []
        
        while head!=None:
           
            if head in l:
                return head
            l.append(head)
            head = head.next
        tmp = ListNode()
        tmp = tmp.next
        return tmp
