class Solution:
    def reverse(self, x: int) -> int:
        if x>(2**31)-1 or x<-(2**31):
            return 0
        s = str(x)
        if s[0]=='-':
            num=int(s[0]+s[1:][::-1])
            if num>(2**31)-1 or num<-(2**31):
                return 0
            else:
                return num
        else:
            x = int(s[::-1])
            if x>(2**31)-1 or x<-(2**31):
                return 0
            else:
                return x
