###sum of amicable numbers under 10000: 31626

print("Upper limit:")
lim=int(input())
i=1
j=1
k=1
tmp=[]
tmp2=[]
tmp_sum=0

amicable=[]

while i < lim:
    ###get all proper factors of i
    j=1
    k=1
    tmp=[]
    tmp2=[]
    while j < i:
        if i%j==0:
           tmp.append(j)
        j+=1
    print(tmp,"::", i)
    ###sum all proper factors of i
    tmp_sum=sum(tmp)
    print("Sum of factors of ", i, ":  ", tmp_sum)
    ###get all proper factors of sum of i factors
    
    if i != tmp_sum:
        while k < tmp_sum:
            if tmp_sum%k==0:
                tmp2.append(k)
            k+=1
    
    
    print(tmp2)
    print("Sum of factors of sum of i factors,", tmp_sum, ":  ", sum(tmp2))
    ###check to see if i and the sum of factors of is factor sum are equal
    if sum(tmp2)==i:
        amicable.append(i)
        amicable.append(sum(tmp2))
        
    i+=1
amicable = list(dict.fromkeys(amicable))
print(amicable)
print(sum(amicable))
