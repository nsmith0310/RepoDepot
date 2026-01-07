class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        g = list((pattern))
        m = str.split(" ")
        l = list(set(g))
        if len(g)!=len(m):return False
        
        
        chars = [set() for x in l]
        
        i = 0
        while i<len(m):
            chars[l.index(g[i])].add(m[i])
            i+=1
        
        for x in chars:
            if len(list(x))>1:
                return False
        
        i = 0
        while i<len(chars)-1:
            j = i+1
            while j<len(chars):
                if chars[i]==chars[j]:return False
                j+=1
            i+=1
        return True
        
        
        
