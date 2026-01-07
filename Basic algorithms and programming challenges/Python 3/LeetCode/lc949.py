from itertools import permutations as p
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        l = list(p(A))
        mx = -1
        r = ""
        for x in l:
            num1 = int(str(x[0])+str(x[1]))
            if num1<24:
                num2 = int(str(x[2])+str(x[3]))
                
                if num2<60:
                    if int(str(x[0])+str(x[1])+str(x[2])+str(x[3]))>mx:
                        
                        mx = int(str(x[0])+str(x[1])+str(x[2])+str(x[3]))
                        
                        r = str(x[0])+str(x[1])+":"+str(x[2])+str(x[3])
            
        return r
