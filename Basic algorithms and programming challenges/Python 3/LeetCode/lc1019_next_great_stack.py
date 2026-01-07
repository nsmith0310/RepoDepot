# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head==None: return []
        l = []
        c=0
        while head!=None:
            l.append(head.val)
            c+=1
            head = head.next
        
        i = c-1
        f = [0 for i in range(c)]
        q = []
        count = 0
        while i>=0:
            while count!=0 and q[-1]<=l[i]:
                del q[-1]
                count-=1
            if count==0:
                f[i]=0
            else:
                f[i]=q[-1]
            q.append(l[i])
            count+=1
            i-=1
    
        return f
