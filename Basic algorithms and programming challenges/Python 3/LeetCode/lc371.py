class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        p1 = 0
        p2 = 0
        if a<0:
            p1 = 1
        if b<0:
            p2 = 1
        
        a = abs(a)
        b = abs(b)
        
        if a==0==b:return 0
        
        num1 = str(bin(a))[2:]
        num2 = str(bin(b))[2:]
        diff = abs(len(num1)-len(num2))
        s=""
        i = 0
        while i<diff:
            s+="0"
            i+=1
        
        if len(num1)>len(num2):
            num2 = s+num2
            
        elif len(num2)>len(num1):
            num1 = s+num1
            
        num1 = num1
        num2 = num2
        
        if p1==p2:
            s = ""
            c = 0
            i = len(num1)-1
            while i>=0:
                if c==0:
                    if num1[i]=='0' and num2[i]=='0':s+='0'
                    elif num1[i]=='0' and num2[i]=='1':s+='1'
                    elif num1[i]=='1' and num2[i]=='0':s+='1'
                    elif num1[i]=='1' and num2[i]=='1':
                        s+='0'
                        c=1
                elif c==1:
                    if num1[i]=='0' and num2[i]=='0':
                        s+='1'
                        c=0
                    elif num1[i]=='0' and num2[i]=='1':
                        s+='0'
                        
                    elif num1[i]=='1' and num2[i]=='0':
                        s+='0'
                        
                    elif num1[i]=='1' and num2[i]=='1':
                        s+='1'
                        
                if i==0 and c==1:s+='1'
                i-=1
            s=s[::-1]
            if p1==0:
                return int(s,2)
            else: return -1*int(s,2)
                    
        else:
            
            i = len(num1)-1
            s=""
            if int(num1,2)==int(num2,2):return 0
            
            l1 = list(map(int,num1))
            l2 = list(map(int,num2))
            
            if int(num1,2)>int(num2,2):
                while i>=0:
                    if l1[i]>=l2[i]:
                        s+=str(l1[i]-l2[i])
                    else:
                        f = 0
                        j = i         
                        while j>=0:
                            if l1[j]==1:
                                f=1
                                break
                            j-=1      
                        if f==1:
                            l1[j]=0
                            k = j+1
                            while k<i:
                                l1[k]=1
                                k+=1
                            l1[k]=2
                            if l1[i]>=l2[i]:
                                s+=str(l1[i]-l2[i])
                    i-=1
                s = s[::-1]
            else:
                
                while i>=0:
                    if l2[i]>=l1[i]:
                        s+=str(l2[i]-l1[i])
                    else:
                        f = 0
                        j = i
                        while j>=0:
                            if l2[j]==1:
                                f=1
                                break
                            j-=1
                        if f==1:
                            l2[j]=0
                            k = j+1
                            while k<i:
                                l2[k]=1
                                k+=1
                            l2[k]=2
                            if l2[i]>=l1[i]:
                                s+=str(l2[i]-l1[i])
                    i-=1
                s = s[::-1]
                
                if a>b and p1==1:
                    return -1*int(s,2)
                if a<b and p1==1:
                    return int(s,2)
                if b>a and p2==1:
                    return -1*int(s,2)
                else:
                    return int(s,2)
                                    
                                    
                                    
                                    
                                    
                
