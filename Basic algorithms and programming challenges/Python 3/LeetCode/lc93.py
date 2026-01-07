class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12 or len(s)<4:
            return []
        
        m = len(s)
        
        pos = []
        
        
        i = 1
        while i<=3:
            j = i+1
            while j<=6 and j<m:
                k = j+1
                while k<m:
                    pos.append([int(s[:i]),int(s[i:j]),int(s[j:k]),int(s[k:])])
                    k+=1
                j+=1
            i+=1
        f = []
        for x in pos:
            t = 0
            for y in x:
                if y>255:
                    t = 1
                    break
            
            if t==0:
                S=""
                for y in x:
                    S+=str(y)+"."
                    
                    if len(S)-4==m:
                        f.append(S[:-1])
        return f
