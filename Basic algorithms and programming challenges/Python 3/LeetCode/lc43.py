class Solution:
    def conv(self, s: str) -> str:
        t = 0
        l = len(s)
        i = 0
        while i<len(s):
            if s[i]=='1':
                t+=1*pow(10,l-i-1)
            if s[i]=='2':
                t+=2*pow(10,l-i-1)
            if s[i]=='3':
                t+=3*pow(10,l-i-1)
            if s[i]=='4':
                t+=4*pow(10,l-i-1)
            if s[i]=='5':
                t+=5*pow(10,l-i-1)
            if s[i]=='6':
                t+=6*pow(10,l-i-1)
            if s[i]=='7':
                t+=7*pow(10,l-i-1)
            if s[i]=='8':
                t+=8*pow(10,l-i-1)
            if s[i]=='9':
                t+=9*pow(10,l-i-1)
            i+=1
        return t
                
    
    
    
    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.conv(num1)*self.conv(num2))
