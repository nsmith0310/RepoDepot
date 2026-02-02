###104743

from euler import rmtest as r
c=0
l=[]
i = 2
while i!=-1:
    if r(i,3)==True:
        l.append(i)
        c+=1
    if c==10001:
        print(l[-1])
        break
    i+=1


'''
###works about as well as the above
print("Prime number in position: ")
pos=int(input())
i = 2
primes=[]
while i < pos+100000:
    j = 2
    while j <= (i/j):
        if not (i%j): break
        j+=1
    if (j > (i/j)): primes.append(i)
    i+=1
print("Prime number in position ", pos, ":")
print(primes[pos-1])
'''
