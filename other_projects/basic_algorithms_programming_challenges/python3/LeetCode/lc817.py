# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        if head==None:return 0
        
        
        l = ""
        
        
        while head!=None:
            
            try:
                ind = G.index(head.val)
                l+="1"
                del G[ind]
            except:
                l+="/"
            head = head.next
        k = l.split("/")
        
        c = 0
        i = 0
        while i<len(k):
            if k[i]!='':
                c+=1
            i+=1
        return c
        
        
