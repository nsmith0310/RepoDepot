# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = ""
        num2 = ""
        
        
        while l1!=None:
            num1+=str(l1.val)
            l1 = l1.next
        while l2!=None:
            num2+=str(l2.val)
            l2 = l2.next
        num = list(str(int(num1[::-1])+int(num2[::-1])))[::-1]
        
        l = [ListNode(int(x)) for x in num]
        
        if len(l)==1:
            return l[0]
        i = 0
        while i<len(l)-1:
            l[i].next=l[i+1]
            i+=1
        return l[0]
        
        
