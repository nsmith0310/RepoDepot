class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        
        
        
        m = [0 for x in range(1,37)]
        
        
        for i in range(1,n+1):
            
            m[sum(list(map(int,list(str(i)))))-1]+=1
            
        c = 0
        mx = max(m)
        i = 0
        while i<len(m):
            if m[i]==mx:
                c+=1
            i+=1
        return c
        
