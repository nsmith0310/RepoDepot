class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0 or num==-0:
            return "0"
        s=""
        k = 0
        if num<0:
            k = 1
            num*=-1
        while num>0:
            s+=str(num%7)
            num//=7
        if k==0:    
            return (s[::-1])
        else:
            return str(-1*int(s[::-1]))
