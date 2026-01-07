class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = ""
        i = 0
        while i<len(S):
            if S[i]!="-":
                s+=S[i]
            i+=1
        if len(s)==0:
            return ""
        if len(S)<K:
            return S
        
        flip = len(s)%K
        
        if flip!=0:
            ind = []
            start = s[:flip].upper()+"-"
            new = list(s[flip:].upper())
            
            j = 1
            while j<len(new)//K:
                ind.append(j*K)
                j+=1
            j = 0
            for x in ind:
                new.insert(x+j,"-")
                j+=1
            return start+''.join(new)
            
                
        else:
            new = list(s.upper())
            ind=[]
            j = 1
            while j<len(new)//K:
                ind.append(j*K)
                j+=1
            j = 0
            for x in ind:
                new.insert(x+j,"-")
                j+=1
            return ''.join(new)
