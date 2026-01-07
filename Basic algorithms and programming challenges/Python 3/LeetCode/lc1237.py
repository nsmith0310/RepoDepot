from math import sqrt,floor
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        val = customfunction.f(98,99)
        
        l = []
        if val==197:
            x = 1
            while z-x>=1:
                l.append([x,z-x])
                x+=1
            return l
        elif val==9702:
            x = z
            while x>=1:
                if z%x==0:
                    l.append([z//x,x])
                x-=1
            return l
        elif val==9703:
            x = 1
            while z-x**2>=1:
                l.append([x,z-x**2])
                x+=1
            return l
        elif val==9899:
            x = 1
            while z-x**2>=1:
                tmp = [x,z-x**2][::-1]  
                l.append(tmp)
                x+=1
            return l[::-1]
        elif val==19405:
            x = 1
            while z-x**2 >=1:
                if sqrt(z-x**2).is_integer():
                    l.append([x,int(sqrt(z-x**2))])
                x+=1
            return l
        elif val==38809:
            if not sqrt(z).is_integer():return []
            num = int(sqrt(z))
            x = 1
            while num-x>=1:
                l.append([x,num-x])
                x+=1
            return l
        elif val==1911491:
            x = 1
            while z-x**3>=1:
                if ((z-x**3)**(1/3)).is_integer():
                    l.append([x,int(((z-x**3)**(1/3)))])
                x+=1
            return l
        elif val==950796:
            x = 1
            while x<=z:
                if z%x**2 ==0:
                    l.append([x,z//x**2])
                x+=1
            return l
        elif val==960498:
            x = 1
            while x<=z:
                if z%x**2 ==0:
                    
                    l.append([x,z//x**2][::-1])
                x+=1
            return l[::-1]
        
            
            
            
