class Solution:
    def maskPII(self, S: str) -> str:
        l = S.split(" ")
        S = ''.join(l)
        
        if "@" in S:
            s1 = S[S.index("@"):]
            s2 = S[:S.index("@")]
            
            mod = s2.lower()
            
            return mod[0]+"*****"+mod[-1]+s1.lower()
        else:
            s = ""
            i = 0
            while i<len(S):
                if S[i]!='(' and S[i]!=')' and S[i]!="-" and S[i]!="+":
                    s+=S[i]
                    
                i+=1
            S = s
            f = ""
            tmp1 = S[-10:]
            tmp2 = S[:-10]
            
            if tmp2!="":
                f+="+"
                i=0
                while i<len(tmp2):
                    f+="*"
                    i+=1
                f+="-"
            return f+"***-***-"+tmp1[-4:]
            
