class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        
        s='1'
        while i<=n-1:
            j = 0
            t=''
            while j<len(s):
                k=j+1
                while k<len(s):
                    if s[j]!=s[k]:
                        break
                    else:
                        k+=1
            
                t=t+str(k-j)+str(s[j])
            
                j+=(k-j)
        
            s=t
        
            i+=1
        return s
