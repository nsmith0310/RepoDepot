class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num1 = str(bin(x))[2:]
        num2 = str(bin(y))[2:]
        
        c = 0
        i = 0
        if len(num1)>len(num2):
            z = abs(len(num1)-len(num2))
            s = ''.join(['0' for k in range(0,z)])
            num2 = s+num2
            short = num2
        elif len(num1)<len(num2):
            z = abs(len(num1)-len(num2))
            s = ''.join(['0' for k in range(0,z)])
            num1 = s+num1
            short = num1
        else:
            short=num1
        
        while i<len(short):
            if num1[i]!=num2[i]:
                c+=1
            i+=1
        return c
