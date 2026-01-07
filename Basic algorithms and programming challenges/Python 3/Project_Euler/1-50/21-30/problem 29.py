###len 2 <= a <= 100, 2<=b<=100, a^b = 9183
print("Enter max base and power value: ")
num=int(input())
a = 2
b = 2
powers=[]
while a <=num:
    b=2
    while b <= num:
        powers.append(pow(a,b))
        b+=1
    a+=1
powers = list(dict.fromkeys(powers))
powers.sort()
print("Length of series generated consisting of unique values: ", len(powers))
        
