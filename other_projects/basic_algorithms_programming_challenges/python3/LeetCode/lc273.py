from math import log, floor

class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        s = []
        
        
        ten = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        ones = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        
        other = ["Thousand","Million","Billion","Trillion","Quadrillion","Quintillion","Sextillion","Septillion","Octillion","Nonillion"]
        
        
        
        s2 = str(num)[::-1]
        c = 0
        while s2!="":
        
            parse = s2[:3]
            if len(parse)>=2:
                t = 0
                if parse[1]=="1":
                    s.append(ten[int(parse[0])])
                    t = 1
                elif parse[1]=='0':
                    if parse[0]!='0':
                        s.append(ones[int(parse[0])-1])
                    t=1
                if t==0:
                    if parse[0]=="0":
                        s.append(tens[int(parse[1])-2])
                    else:
                        s.append(ones[int(parse[0])-1])
                        s.append(tens[int(parse[1])-2])
            else:
                s.append(ones[int(parse[0])-1])
            if len(parse)==3 and parse[2]!='0':
                
                s.append("Hundred")
                s.append(ones[int(parse[2])-1])
                
            s2=s2[3:]
            
            if s2!="":
                s.append(other[c])
            c+=1
        ###print(s)
        lim = len(s)
        
        i = 0
        while i<len(s)-1:
            if s[i] in other and s[i+1] in other:
                del s[i]
                i-=1
            i+=1
        
        s = s[::-1]
        
        
        f = ' '.join(s)
        
        return f
            
            
            
            
            
            
            
            
            
                    
                
            
            
            
