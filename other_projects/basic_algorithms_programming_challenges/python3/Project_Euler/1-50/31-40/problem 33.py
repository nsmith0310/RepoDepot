###just need to reduce the fraction to lowest terms
###answer: 100 or 387296/38729600 = 1/100

i = 10
j = 10


num=[]
demon=[]
num_prod = 1
demon_prod = 1


while i <= 99:
    j=10
    while j <=99:
        if str(i)[1] == str(j)[0] and str(i)[0] != str(j)[1]:
            if str(j)[0] !="0" and str(j)[1] !="0":
                if (i/j) == float(str(i)[0])/float(str(j)[1]):
                    num.append(i)
                    print(i)
                    demon.append(j)
                    print(j)
        j+=1
    i+=1


i = 0
while i < len(num):
    num_prod = num_prod * num[i]
    i+=1

    
m = 0
while m < len(demon):
    demon_prod = demon_prod*demon[m]
    m+=1

print(str(num_prod),"/",str(demon_prod),"=","1/",demon_prod/num_prod)

