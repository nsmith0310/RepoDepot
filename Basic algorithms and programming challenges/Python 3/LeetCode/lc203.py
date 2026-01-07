# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None: return head
        l = []
        
        while head != None:
            if head.val!=val:
                l.append(ListNode(head.val))
            head = head.next
        if len(l)==0:
            tmp = ListNode()
            tmp = tmp.next
            return tmp
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            i+=1
        return l[0]
