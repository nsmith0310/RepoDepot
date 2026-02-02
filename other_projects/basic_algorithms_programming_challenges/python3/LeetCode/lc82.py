# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:return None
        
        l = []
        
        while head!=None:
            l.append(head.val)
            head = head.next
            
        l.sort()
        b = list(set(l))
        
        f = []
        for x in b:
            if l.count(x)==1:
                f.append([x,ListNode(x)])
        f.sort(key=lambda x: x[0])
        if f==[]:
            tmp = ListNode()
            tmp = tmp.next
            return tmp
        elif len(f)==1:
            return f[0][1]
        
        i = 0
        while i<len(f)-1:
            f[i][1].next = f[i+1][1]
            i+=1
        
        return f[0][1]
        
