class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        num1 = ''.join(list(map(str,arr1)))[::-1]
        num2 = ''.join(list(map(str,arr2)))[::-1]
        
        p1 = len(num1)
        p2 = len(num2)
        
        
        t1 = 0
        t2 = 0
        
        i = 0
        while i<p1:
            t1+=int(num1[i])*pow(-2,i)
            i+=1
        
        
        i = 0
        while i<p2:
            t2+=int(num2[i])*pow(-2,i)
            i+=1
            
        print(t1,t2)
       
        N = t1+t2
        tmp = N
        s = ""
        if N==0:return [0]
        
        while N!=0:
            if N%-2==-1:
                s+="1"
                N = (N-1)//-2
                
            else:
                s+=str(N%-2)
                N//=-2
                
        
        r = list(s[::-1])
        return r
            
        
        
        
