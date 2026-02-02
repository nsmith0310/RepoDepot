###Answer: long 997651

from euler import primes

p = primes(1000000)
mx=0
for x in p[int(len(p)*.5):]:
    i = len(p)-1
    while i >=0:
        count = 0
        if x - p[i]>0:
            j = i
            y = x
            while y - p[j]>=0:
                y = y - p[j]
                count+=1
                if y == 0:
                    ###print(x,count)
                    if count>mx:
                        mx = count
                        top = x
                    break
                
                j-=1      
        i-=1
print(top)

                
