class Solution:
    def sortString(self, s: str) -> str:
        l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        t = 0
        counts=[]
        for x in l:
            p = s.count(x)
            if p!=0:
                counts.append([x,p])
            t+=p
        
        S=""  
        while t>0:
            i = 0
            while i<len(counts):
                if counts[i][1]>0:
                    S+=counts[i][0]
                    counts[i][1]-=1
                    t-=1
                i+=1
            if t==0:
                break
            i = len(counts)-1
            while i>=0:
                if counts[i][1]>0:
                    S+=counts[i][0]
                    counts[i][1]-=1
                    t-=1
                i-=1
            if t==0:
                break
        return S    
        
            
