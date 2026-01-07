class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        d = dict()
        mx = 0
        
        i = 0
        while i<=len(s)-minSize:
            tmp = s[i:i+minSize]
            if len(list(set(list(tmp))))<=maxLetters:
                ###print(tmp)
                try:
                    d[tmp]+=1
                    if d[tmp]>mx:
                        mx = d[tmp]
                except:
                    d[tmp]=1
                    if d[tmp]>mx:
                        mx = d[tmp]
            i+=1
        return mx
        
            
