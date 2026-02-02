###answer 648
from math import factorial
fact = str(factorial(100))
lst = list(fact)
numbers = [ int(x) for x in lst ]
###print(numbers)
print("Sum of 100!:", sum(numbers))
