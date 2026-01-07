# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        
        
        while head!=None:
            s+=str(head.val)
            head = head.next
            
        return int(s,2)
