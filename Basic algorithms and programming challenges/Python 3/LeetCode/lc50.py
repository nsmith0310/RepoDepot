class Solution:
    def power(self, a: float, n: float) -> float:


        if n==0:
            return 1
        if n==1:
            return a
        if n==2:
            return a**2
        if n%2==0:
            return (((a**2))**((n/2)))
        else:
            return (a*((a**2))**(((n-1)/2)))
    def myPow(self, x: float, n: int) -> float:
        return self.power(1.0*x,1.0*n)
