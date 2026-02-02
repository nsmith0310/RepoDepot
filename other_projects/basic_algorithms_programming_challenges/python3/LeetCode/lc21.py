# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        
        nums = []
        if l1==None and l2==None: return l1
        if l1!=None:
            while l1!=None:
                nums.append(l1.val)
                l1 = l1.next
        if l2!=None:
            while l2!=None:
                nums.append(l2.val)
                l2 = l2.next
            
        nums.sort()
        for x in nums:
            l.append(ListNode(x))
        
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            i+=1
        return l[0]
