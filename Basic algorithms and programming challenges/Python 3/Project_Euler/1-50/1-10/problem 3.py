###answer: 6857 (found by trial and error and checking correct answer)
###I just continued toying with the counter and low bound until I began
###getting primes, and I checked the highest one against the listed answer

###using rho
from euler import large_factorize as f

print(int(max(f(600851475143))))

'''



from math import floor
print("Enter number: ")
max_val = int(input())

primes=[]

i=floor(max_val/2)
j = 2

while i >=2:
    j = 2
    while j <= (i/j):
        if not (i%j): break
        j+=1
    if (j > (i/j)):
        if max_val%i==0:
            print(i)
            break
    i-=1

'''
