i = 0
j= 0
k = []
l = []

while i < 1000:
    k.append(i)
    i+=1

while j < len(k):
    if k[j]%3 == 0 or k[j]%5==0:
        l.append(k[j])
    j+=1

print("Sum of natural numbers from 1 to 1000 divisible by 3 or 5: ", sum(l))

