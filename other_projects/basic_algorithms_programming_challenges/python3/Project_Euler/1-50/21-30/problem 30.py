###Answer: 443839
print("Which power?")
power=int(input())
i = 0
j=0
found=[]
while i <=1000000:
    j=0
    tmp2=[]
    tmp = list(str(i))
    tmp = list(map(int, tmp))
    while j < len(tmp):
        tmp2.append(pow(tmp[j], power))
        j+=1
    if sum(tmp2)==i:
        found.append(i)
    i+=1
print(found)
print("Sum: ", sum(found)-1)
    
    
    
