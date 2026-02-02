###answer: 303963552391.0 slowish


###prime factorization algorithm is not mine whatsoever

import math
def primeFactors(n): 
    facts=[]
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        
        facts.append(2)
        n = n / 2
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            facts.append(i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        facts.append(n)
    return facts
i=2
count = 0
while i <= 1000000:
    tmp = primeFactors(i)
    tmp = list(dict.fromkeys(tmp))
    tot=i
    for x in tmp:
        tot-=tot//x
    count+=tot
    i+=1
print(count)
