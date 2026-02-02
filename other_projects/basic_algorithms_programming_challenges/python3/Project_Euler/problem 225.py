###long 2009

###massive help from OEIS
###it seems like the way to exclude a number is to discover a tentative number
###in the list of excluded numbers which the former number is a divisor (this
###potentially marks the former as a definitive non-factor)
###the answer varies with the list lengths because the longer the list, the
###greater the chance of finding a number which our target odd number divides

i = [1,1,1]

j=0

while len(i)<=30000:
    i.append(i[-1]+i[-2]+i[-3])

count=0

j = 1
while j<=2500:
    t=[]
    for x in i:
        t.append(x%j)
    if 0 not in t:
        count+=1
    if count==124:
        print(j)
        break
    j+=2
