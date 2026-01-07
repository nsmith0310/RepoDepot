class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s = ""
        
        i = 0
        while i<len(S)-1:
            p = 1
            j = i+1
            while j<len(S):
                if S[j]==")":
                    p-=1
                else:
                    p+=1
                if p==0:
                    s+=S[i+1:j]
                    break
                j+=1
                    
            i=j+1
        
        return s
