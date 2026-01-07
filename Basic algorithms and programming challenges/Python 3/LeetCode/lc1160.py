class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        f=[]
        for x in words:
            t = 0
            l = set(list(x))
            l2 = [[y,x.count(y)] for y in l]
            for y in l2:
                if chars.count(y[0])<y[1]:
                    t = 1
                    break
            if t == 0:
                f.append(x)
        total = 0
        
        for x in f:
            total+=len(x)
        return total
                
            
                    
                
                    
