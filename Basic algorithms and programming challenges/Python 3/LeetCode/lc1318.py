class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        A = str(bin(a))[2:]
        B = str(bin(b))[2:]
        C = str(bin(c))[2:]
        
        strs = [A,B,C]
        lens=[len(A),len(B),len(C)]
        
        ready = []
        lead = max(lens)
        
        for x in strs:
            s = x
            while len(s)<lead:
                s = "0"+s
            ready.append(s)
            
        A = ready[0]
        B = ready[1]
        C = ready[2]
        
        c = 0
        i = len(C)-1
        while i>=0:
            
            if A[i]=='1' and B[i]=='1' and C[i]=='0':
                c+=2
            elif (A[i]=='1' and B[i]=='0' and C[i]=='0') or (A[i]=='0' and B[i]=='1' and C[i]=='0'):
                c+=1
            elif A[i]=='0' and B[i]=='0' and C[i]=='1':
                c+=1
            i-=1
        return c
            
        
            
