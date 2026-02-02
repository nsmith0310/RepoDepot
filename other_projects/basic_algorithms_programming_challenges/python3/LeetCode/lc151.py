class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = s.split()
        i = 0
        while i<len(s2):
            if " " in s2[i]:
                del s2[i]
            i+=1
        l = len(s2)-1
        
        s3=""
        while l>=0:
            s3+=s2[l]+" "
            l-=1
        return s3[:-1]
