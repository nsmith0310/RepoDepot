###answer: long 26241

from euler import factorize
count = 1
odd = 3

o=0
a=1
l = 1
while l!=-1:
    while odd <=l:
        while count < odd*odd:
            count = count + (odd-1)
            a+=1
            if len(factorize(count))==1:
                o+=1
        odd+=2
    
    if l > 3 and float((o/a))<.10:
        print(l)
        break
    l+=1
