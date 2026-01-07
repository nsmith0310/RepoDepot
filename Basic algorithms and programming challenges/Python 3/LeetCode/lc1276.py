class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t = tomatoSlices
        c = cheeseSlices
        
        
        y = -((t-4*c)/2)
        
        if not y.is_integer():
            return []
        elif c-y<0 or y<0:
            return []
        else:
            y = int(y)
            return [c-y,y]
