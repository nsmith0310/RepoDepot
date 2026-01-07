#answer: (not efficient) 232792560
i = 1
j = 1
count=0

while i != -1:
    count=0
    j = 1
    while j <= 20:
        if i%j == 0:
            count+=1
        j+=1
    if count ==20:
        print(i)
        break
    i+=1
