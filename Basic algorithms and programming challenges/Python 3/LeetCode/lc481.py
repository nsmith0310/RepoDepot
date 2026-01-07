class Solution:
    def magicalString(self, n: int) -> int:
        if n==0:return 0
        if n<=3:
            return 1
        total = 1
        c = 3
        seq = [1,2,2]
        i = 3
        while c<=n:
            num = seq[i-1]
            
            if c+num>n:
                
                if i%2!=0:
                
                
                    total+=n-c
                    
            else:
                if i%2==0:
                    j = 0
                    while j<num:
                        seq.append(2)
                        j+=1
                else:
                    total+=num
                    j = 0
                    while j<num:
                        seq.append(1)
                        j+=1
                
                
            
            
            c+=num    
            i+=1
      
        return total
                
                
                
                
