# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head==None:return head
        
        l = []
        l2 = []
        
        while head!=None:
            j = 0
            while j<len(l2) and head.val>l2[j]:
                j+=1
            
            
            l2.insert(j,head.val)
            l.insert(j,ListNode(head.val))
            head = head.next
            
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            i+=1
        return l[0]
