class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        S = list(s)
        
        
        m = list(set(S))
        
        t = []
        
        for x in m:
            tmp = ""
            j = 0
            while j<k:
                tmp+=x
                j+=1
            t.append(tmp)
            
            
        kill = 0
        while kill==0:
            p = 0
            for x in t:
                
                while x in s:
                    ind = s.index(x)
                    del S[ind:ind+k]
                    p = 1
                    s=''.join(S)
            if p==0:
                break
        return s
                    
                
            
