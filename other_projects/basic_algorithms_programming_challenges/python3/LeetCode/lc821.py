class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        s = list(S)
        c = C
        lc=[]
        li=[]
        i = 0
        while i<len(s):
            if s[i]==c:
                lc.append(i)
            i+=1
        i=0
                
        while i<len(s):
            if s[i]==c:
                li.append(0)
            else:
                tmp = [abs(i-x) for x in lc]
                li.append(min(tmp))
            i+=1
        return li
                    
