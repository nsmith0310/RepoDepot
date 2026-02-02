# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        l = []
        
        
        c = 0
        tmp = []
        while head!=None:
            c+=1
            
            if c>=m and c<=n:
                tmp.append(ListNode(head.val))    
            else:
            
                l.append(ListNode(head.val))
            head = head.next
        tmp = tmp[::-1]
        
        ins = m-1
        for x in tmp:
            l.insert(ins,x)
            ins+=1
        i = 0
        while i<len(l)-1:
            l[i].next = l[i+1]
            i+=1
        return l[0]
