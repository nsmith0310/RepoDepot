class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
       
        
        start = []
        end = []
        
        for x in paths:
            start.append(x[0])
            end.append(x[1])
        for x in end:
            if x not in start:
                return x
        
                
