# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s = ""
        while l1 != None:
            s+=str(l1.val)
            l1 = l1.next        
        t = ""
        while l2 != None:           
            t+=str(l2.val)
            l2 = l2.next
        
        num = list(map(int,list(str(int(s)+int(t)))))
        
        l3 = ListNode(num[0])
        
        l4 = [ListNode(x) for x in num]
        
        i = 0
        while i<len(l4)-1:
            l4[i].next = l4[i+1]
            i+=1
        return l4[0]
