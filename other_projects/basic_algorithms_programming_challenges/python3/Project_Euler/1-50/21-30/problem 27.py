###Answer: -59231

i=-1000
j=-999
mx=0
i_m=0
j_m=0
coef=0
count=0



def get_count(i,j):
    count = 0
    a = i
    b = j
    n = 0
    x = n*n + b*n + a
    test = pow(2,(abs(x)-1))%abs(x)
    while test==1 and x !=0:
        test = pow(2,(abs(x)-1))%abs(x)
        x = n*n + b*n + a
        count+=1
        n+=1
        
    return count-2
    
while i <=1000:
    j=-999
    while j <999:
        count=0
        n=0
        x = n*n + j*n + i
        if x!=0 and pow(2,(abs(x)-1))%abs(x)==1:
            count = get_count(i,j)     
            if count>mx:
                mx=count
                i_m=i
                j_m=j
                coef=i_m*j_m
        j+=1
    
    i+=1
print("i=",i_m,"; j=",j_m,"; number of primes: ",mx)
print("product of coefficients: ", coef)
