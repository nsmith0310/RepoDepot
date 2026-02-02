from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z> x+y:
            return False
        if z==x or z==y or z==0:
            return True
        
        return (1.0*z/gcd(x,y)).is_integer()
            
        
        
        
