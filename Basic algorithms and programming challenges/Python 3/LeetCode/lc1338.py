class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        s = len(arr)
        size = s//2
        c=0
        l = list(set(arr))
        if len(l)==len(arr):
            return size
        l2 = [[x,arr.count(x)] for x in l]
        while size>0:
            
            mn = 10**5 + 1
        
            i = 0
            while i<len(l2):
                t = abs(size-l2[i][1])
                if t<=mn:
                    mn = t
                    d = l2[i][1]
                    d2 = i
                if mn==0:
                    break
                i+=1
                
            
            c+=1
            
            del l2[d2]
            size-=d
            
            
        return c
