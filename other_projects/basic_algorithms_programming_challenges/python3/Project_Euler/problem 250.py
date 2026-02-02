###long 1425480602091519
###based mainly on a translation of a mathematica program
###by nayuki (the method used seems to be common, but I am still
###not sure why it works)

from euler import pmod

m = 250
lim = 250250


s=[]
i = 0
while i<=m:
    if i==m:
        s.append(1)
    else:
        s.append(0)
    i+=1

q=10**16
for k in range(1,lim+1):
    ###main point of confusion (besides the modulo)
    s = [s[j]%q+(s[j-pmod(k,k,m)]%q)%q for j in range(m)]
print((s[0]+s[-1]-1)%q)
