# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None: return True
        l = []
        
        while head!=None:
            l.append(str(head.val))
            head = head.next
        if len(l)%2==0:
            l1 = l[:len(l)//2]
            l2 = l[len(l)//2:][::-1]
        
            return l1==l2
        else:
            l1 = l[:len(l)//2]
            l2 = l[len(l)//2 + 1:][::-1]
        
            return l1==l2
