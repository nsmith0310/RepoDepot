class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        
        
        t = [0,0,0]
        i = 0
        while i<len(bills):
            if bills[i]==5:
                t[0]+=1
            elif bills[i]==10:
                if t[0]==0:
                    return False
                else:
                    t[1]+=1
                    t[0]-=1
            elif bills[i]==20:
                if t[1] >=1 and t[0]>=1:
                    t[1]-=1
                    t[0]-=1
                    t[2]+=1
                elif t[0]>=3:
                    t[0]-=3
                    t[2]+=1
                else:
                    return False
            i+=1
        return True
            
            
