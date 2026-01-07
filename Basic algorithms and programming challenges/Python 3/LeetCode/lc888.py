class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA = sum(A)
        sumB = sum(B)
        
        uA = list(set(A))
        uB = list(set(B))
        
        f = []
        
        for x in uA:
            tmp = -.5*sumA + x + .5*sumB
            if tmp.is_integer() and tmp in uB:
                return [x,int(tmp)]
            
        
       
        
