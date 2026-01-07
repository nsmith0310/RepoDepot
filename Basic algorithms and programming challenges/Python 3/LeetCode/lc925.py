class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        
        a = list(name)
        b = list(typed)
        
        counts = []
        
        countsb = []
        
        if len(a)==1:
            return list(set(b))==a
                
        i = 0
        while i<len(a):
            
            c = 1
            j = i+1
            while j<len(a) and a[j]==a[i]:
                c+=1
                j+=1
            counts.append([a[i],c])
            i+=c
        ###print(counts)
        if len(b)<len(a): return False
        
        try:
            i = 0
            while i<len(b):
            
                c = 1
                j = i+1
                while j<len(b) and b[j]==b[i]:
                    c+=1
                    j+=1
                ###print(b[i],c,counts)
                
                if b[i]!=counts[0][0] or c<counts[0][1]:return False
                del counts[0]
                i+=c
        except:
            return False
        if counts!=[]:
            return False
        return True
            
