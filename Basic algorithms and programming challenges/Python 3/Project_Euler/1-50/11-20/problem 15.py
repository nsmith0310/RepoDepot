###answer: 137846528820
from math import factorial

print("Enter dimension A of AxA:")
dim = int(input())

print(int(factorial(2*dim)/factorial((dim))**2))
