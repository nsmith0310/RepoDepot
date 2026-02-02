class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        i = 1
        while i<=n:
            if i%5==0 and i%3==0:
                l.append("FizzBuzz")
            elif i%5==0:
                l.append("Buzz")
            elif i%3==0:
                l.append("Fizz")
            else:
                l.append(str(i))
            i+=1
        return l
