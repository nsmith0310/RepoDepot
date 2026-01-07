###long: 2129970655314432
###method described on mathexchange by user looking for a faster
###method

from euler import tenton as b,prod

###convert row number to base (7), add 1 to each digit of result,
###and multiply these numbers to get count of numbers in said row
###not divisible by 7
def f(n):
    return prod([k+1 for k in list(map(int,list(str(b(n,7)))))])

i=1
t = 1
while i<10**9:
    t+=f(i)
    i+=1
print(t)
