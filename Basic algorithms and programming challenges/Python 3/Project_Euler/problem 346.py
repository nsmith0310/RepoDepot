###336108797689259276


###f is not my function (I corrected the syntax and made a few tweaks)
def f(s,base):
    llen = len(s)
    power = 1 #Initialize power of base
    num = 0     #Initialize result
    # Decimal equivalent is str[len-1]*1 + 
    # str[len-1]*base + str[len-1]*(base^2) + ... 
    for i in range(llen - 1, -1, -1):
        # A digit in input number must 
        # be less than number's base 
        if int(s[i]) >= base:
            return 0
        num += int(s[i]) * power
        power = power * base
    return int(num)

def power(a,b):
    if b&1==True:
        return a*(a**2)**int((b-1)/2)
    else:
        return (a**2)**int(b/2)

def rep(n):
    return str((power(10,n)-1)//9)

###A000225
t = [0,1]
while t[-1]<10**12:
    t.append(t[-1]+2*t[-2]+2)
nums=list(t)

i = 3
while i<=40:
    j = 1
    while j!=-1:
        m = f(rep(i),j)
        if int(m) <10**12:
            if int(m)!=0:
                nums.append(int(m))
        else:
            
            break
        j+=1
    i+=1
f=[]
for x in nums:
    if x<10**12:
        f.append(x)
f.sort()

print(sum(list(set(f)))-3)
