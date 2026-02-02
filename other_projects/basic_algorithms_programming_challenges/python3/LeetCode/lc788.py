class Solution:
    def rotatedDigits(self, N: int) -> int:
       
        l = [i for i in range(1,N+1)]
        final=[]
        for y in l:
            x = str(y)
            t=0
            s1 = list(x)
            s= ""
            i = 0
            while i<len(x):
                if x[i]=='0':
                    s+='0'
                elif x[i]=='1':
                    s+='1'
                elif x[i]=='2':
                    s+='5'
                elif x[i]=='3':
                    t=1
                    break
                elif x[i]=='4':
                    t=1
                    break
                elif x[i]=='5':
                    s+='2'
                elif x[i]=='6':
                    s+='9'
                elif x[i]=='7':
                    t=1
                    break
                elif x[i]=='8':
                    s+='8'
                elif x[i]=='9':
                    s+='6'
                i+=1
            if t==0:
                if s!=''.join(s1):
                    final.append(int(''.join(s1)))
        return len(final)
