###answer: 7295372

d = 2
n = 1
tmp=[]
while d <= 12000:
    n = 1
    while n < d:
        if (n/d) > (1/3) and (n/d) < (1/2):
            tmp.append(n/d)
        n+=1
    d+=1
tmp = list(dict.fromkeys(tmp))
print(len(tmp))
