class Solution:
    def countSegments(self, s: str) -> int:
        k = s.split(" ")
        c=0
        i = 0
        while i<len(k):
            if k[i]!='':
                c+=1
            i+=1
        return c
