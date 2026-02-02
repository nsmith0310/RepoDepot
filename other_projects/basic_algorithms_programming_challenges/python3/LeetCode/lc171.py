class Solution:
    def titleToNumber(self, s: str) -> int:
        
    
        
    
        S = s.lower()
        if len(S)==1:
            return ord(S)-96
        l = list(S)
        
        t=26*(ord(l[0])-96) + ord(l[1])-96
        
        
        i = 2
        while i<len(l):
            t*=26
            
            t+=ord(l[i])-96
            i+=1
        return t
            
            
