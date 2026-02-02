###long 932718654

from itertools import permutations
t = list(permutations(['1','2','3','4','5','6','7','8','9']))
q=[]
for x in t:
    q.append(int(''.join(x)))
q.sort(reverse=True)

'''def test(n):'''
    




mx=0
i = 1
while i<=10000:
    j = 1
    while j <= 9:
        k = 1
        n=""
        while k <=j:
            n+=str(k*i)
            k+=1
        if int(n)in q:
            ###print(int(n))
            if int(n)>mx:
                mx=int(n)
        j+=1
    i+=1
print(mx)
        
    
    
