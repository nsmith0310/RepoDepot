###long 676333270

from euler import rmtest

def test(n):

 

    num1 = pow(n,2)+1

    num2 = pow(n,2)+3

    num3 = pow(n,2)+7

    num4 = pow(n,2)+9

    num5 = pow(n,2)+13

    num6 = pow(n,2)+27

   

    if rmtest(num1,3)==True and rmtest(num2,3)==True and rmtest(num3,3)==True and rmtest(num4,3)==True and rmtest(num5,3)==True and rmtest(num6,3)==True:

        z=[num1,num2,num3,num4,num5,num6]

    else:

        return False

    t=[]

    i = z[0]

    while i<=z[len(z)-1]:

        if i not in z:

            t.append(i)

        i+=1

    for x in t:

        if rmtest(x,3)==True:

            return False

    return True

   

i = 1

total=0

while i<=150000000:

    if test(i)==True:

        total+=i

    i+=1

print(total)
