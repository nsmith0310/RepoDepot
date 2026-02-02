class Solution:
    def maximumSwap(self, num: int) -> int:
        
        if num<11:
            return num
        
        pos = [num]
        
        l1 = list(str(num))
        n = str(num)
        
        i = 0
        while i<len(l1):
            j = 0
            while j<len(n):
                if i!=j:
                    m = [x for x in l1]
                    
                    m[i]= n[j]
                    m[j]=n[i]
                    pos.append(int(''.join(m)))
                j+=1
            i+=1
        return max(pos)
            
        
        
