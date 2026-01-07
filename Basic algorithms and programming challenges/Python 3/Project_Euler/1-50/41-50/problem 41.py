###max: 7652413 for num <=9 (ANSWER)


def is_prime(integers):
    i = integers
    mx =0
    for x in i:
        if pow(2,(x-1))%x==1:
            mx = x
            break
    return mx

import itertools
print("Test limit:")
num=int(input())
tmp=[]
panprime=[]
i=1
maximum=0
while i <= num:
    perms=[]
    tmp.append(str(i))
    integers=[]
    perms=list(itertools.permutations(tmp))
    for x in perms:
        integers.append(int(''.join(x)))
    integers.sort(reverse=True)
    maximum = is_prime(integers)
    print(maximum)
    i+=1

print(maximum)
    
