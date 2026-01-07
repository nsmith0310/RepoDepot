class Solution:
    def findComplement(self, num: int) -> int:
        s = str(bin(num))[2:]
        s2=""
        i = 0
        while i<len(s):
            if s[i]=='0':
                s2+='1'
            else:
                s2+='0'
            i+=1
        return int(s2,2)
