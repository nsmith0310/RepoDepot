###answer: 9110846701
series=[]

i = 0
while i <= 1000:
    series.append(pow(i,i))
    i+=1
    
tmp = str(sum(series))[::-1][:10][::-1]
print(int(tmp))

